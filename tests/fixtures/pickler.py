import pickle
import requests
from requests import Response
from pathlib import Path
from typing import Any


def pickle_response( filename: str, data: Any ) -> None:
    fixture_path = f"/tests/fixtures/{filename}.pkl"
    file_path = str( Path.cwd() ) + fixture_path

    with open( file_path, "wb" ) as file:
        pickle.dump( data, file )


def unpickle_response( filename: str ) -> Response:
    fixture_path = f"/tests/fixtures/{filename}.pkl"
    file_path = str( Path.cwd() ) + fixture_path

    with open( file_path, "rb" ) as file:
        return pickle.load( file )


def pickle_valid_title_search_response() -> None :
    url = "https://rest.imdbapi.dev/v2/search/titles?query=bambi"
    response = requests.get( url )
    pickle_response( "valid_title_search_response", response )


def pickle_invalid_title_search_response() -> None:
    url = "https://rest.imdbapi.dev/v2/search/titles?query=__invalid__request__"
    response = requests.get( url )
    pickle_response( "invalid_title_search_response", response )


def pickle_valid_imdb_id_response() -> None:
    url = "https://rest.imdbapi.dev/v2/titles/tt3205278"
    response = requests.get( url )
    pickle_response( "valid_imdb_id_response", response )


def pickle_invalid_imdb_id_response() -> None:
    url = "https://rest.imdbapi.dev/v2/titles/tt-INVALID-ID"
    response = requests.get( url )
    pickle_response( "invalid_imdb_id_response", response )


def pickle_valid_webscrapping_response() -> None:
    url = f"https://www.metacritic.com/movie/bambi/"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get( url, headers=user_agent )
    pickle_response( "valid_webscrapping_response", response )


if __name__ == "__main__":
    pickle_valid_title_search_response()
    pickle_invalid_title_search_response()
    pickle_valid_imdb_id_response()
    pickle_invalid_imdb_id_response()
    pickle_valid_webscrapping_response()

