"""
Internet Movie Database Access

Implements the SearchTitle, Reviews, and Ratings APIs
"""
import logging
import requests

logger = logging.getLogger()

class IMDb:
    """Access the Internet Movie database"""

    __BASE_URL = "https://rest.imdbapi.dev/v2"

    def search_titles( self, title: str ) -> dict:
        """Search for a movie by Title"""
        logger.info( f"Searching IMDb for Title: {title}" )
        response = requests.get( f"{self.__BASE_URL}/search/titles?query={title}" )
        if response.status_code != 200:
            return {}
        return response.json().get( "titles", {} )

    def movie_reviews( self, title: str ) -> dict:
        """Get reviews for a movie"""
        logger.info( f"Searching IMDb for Reviews: {title}" )
        response = requests.get( f"{self.__BASE_URL}/search/titles?query={title}" )
        if response.status_code == 200:
            return response.json()
        return {}

    def movie_ratings(self, imdb_id: str) -> dict:
        """Get ratings for a movie"""
        logger.info("Searching IMDb for Ratings: %s", imdb_id)
        response = requests.get(f"https://imdb-api.com/API/Ratings/{self.apikey}/{imdb_id}")
        if response.status_code == 200:
            return response.json()
        return {}
