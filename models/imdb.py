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

    def search_titles( self, title: str ) -> dict:
        """Search for a movie by Title"""
        logger.info( f"Searching IMDb for Title: {title}" )
        response = requests.get( f"{self.__BASE_URL}/search/titles?query={title}" )
        if response.status_code != 200:
            return []
        return response.json().get( "titles", [] )

    def movie_ratings(self, imdb_id: str) -> dict:
        """Get ratings for a movie"""
        logger.info("Searching IMDb for Ratings: %s", imdb_id )
        response = requests.get( f"{self.__BASE_URL}/titles/{imdb_id}" )

        results = response.json()
        null_results = {
            "id": None, "primary_title": None, "rating": None
        }

        if "code" in results:
            return null_results

        return {
            key : value
            for key, value in response.json().items()
            if key in null_results
        }

    def movie_reviews( self, imdb_id: str ) -> dict:
        """Get reviews for a movie"""
        titles = self.search_titles( imdb_id )
        title = titles[ 0 ][ "original_title" ]
        print( f"GOT TITLE:\t{title}" )

        logger.info( f"Searching IMDb for Reviews: {title}" )
        title = title.replace( " ", "-" ).replace( ":", "" ).lower()
        print( "FORMATTED TITLE" )

        url = f"https://www.metacritic.com/movie/{title}/"
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get( url, headers=user_agent )
        print( "SCRAPPING DONE" )

        if response.status_code != 200:
            return { "reviews": [] }
        return self._webscrape_reviews( response )

    def _webscrape_reviews( self, response: Response ) -> dict:
        """Scrap reviews on the landing page of `title`"""
        soup = bs4.BeautifulSoup( response.content, "html.parser" )

        name = "div"
        attrs = { "class": "c-siteReview_quote g-outer-spacing-bottom-small" }

        reviews_raw = soup.find_all( name, attrs )
        reviews = { "reviews": [] }

        span_start = "<span>"
        span_end = "</span>"

        for review in reviews_raw:
            review = str( review )
            start = review.find( span_start ) + len( span_start )
            end = review.find( span_end )

            reviews[ "reviews" ].append( review[ start : end ])

        return reviews
