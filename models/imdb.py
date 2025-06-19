"""
Internet Movie Database Access

Implements the SearchTitle, Reviews, and Ratings APIs
"""
import bs4
import logging
import requests
from requests import Response


logger = logging.getLogger()


class IMDb:
    """Access the Internet Movie database"""

    __BASE_URL = "https://rest.imdbapi.dev/v2"
    __NULL_RESULTS = {
        "id": None, "primary_title": None, "rating": None
    }

    def search_titles( self, title: str ) -> dict:
        """Search for a movie by Title"""
        logger.info( f"Searching IMDb for Title: {title}" )
        response = requests.get( f"{self.__BASE_URL}/search/titles?query={title}" )
        if response.status_code != 200:
            return []
        return response.json().get( "titles", [] )

    def _is_valid_imdb_id( self, imdb_id: str ) -> list:
        response = requests.get( f"{self.__BASE_URL}/titles/{imdb_id}" )
        return [ "code" not in response.json(), response ]

    def movie_ratings( self, imdb_id: str) -> dict:
        """Get ratings for a movie"""
        logger.info( "Searching IMDb for Ratings: %s", imdb_id )
        is_valid_imdb_id, response = self._is_valid_imdb_id( imdb_id )

        if not is_valid_imdb_id:
            return self.__NULL_RESULTS

        return {
            key : value
            for key, value in response.json().items()
            if key in self.__NULL_RESULTS
        }

    def movie_reviews( self, imdb_id: str ) -> dict:
        """Get reviews for a movie"""
        logger.info( "Searching MetaCritic for Reviews: %s", imdb_id )
        is_valid_imdb_id, _ = self._is_valid_imdb_id( imdb_id )

        if not is_valid_imdb_id:
            return { "reviews": [] }

        titles = self.search_titles( imdb_id )
        title = titles[ 0 ][ "original_title" ]
        title = title.replace( " ", "-" ).replace( ":", "" ).lower()
        return self._webscrape_reviews( title )

    def _webscrape_reviews( self, title: str ) -> dict:
        """Scrap reviews on the landing page of `title`"""
        reviews = { "reviews": [] }

        url = f"https://www.metacritic.com/movie/{title}/"
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get( url, headers=user_agent )

        if response.status_code != 200:
            return reviews

        soup = bs4.BeautifulSoup( response.content, "html.parser" )

        name = "div"
        attrs = { "class": "c-siteReview_quote g-outer-spacing-bottom-small" }
        reviews_raw = soup.find_all( name, attrs )

        span_start = "<span>"
        span_end = "</span>"

        for review in reviews_raw:
            print( "\n\n\n" + str( review ) + "\n\n\n" )
            review = str( review )
            start = review.find( span_start ) + len( span_start )
            end = review.find( span_end )

            reviews[ "reviews" ].append( review[ start : end ])

        return reviews
