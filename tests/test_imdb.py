"""Test Cases for Mocking Lab"""
from requests.exceptions import ConnectionError
from requests import Response
from unittest.mock import patch, Mock
from pathlib import Path
import pytest
import json


from models import IMDb


@pytest.fixture( scope="session" )
def response_data():
    fixture_path = "/tests/fixtures/imdb_responses.json"
    file_path = str( Path.cwd() ) + fixture_path

    with Path( file_path ).open() as file:
        return json.load( file )


@pytest.fixture( scope="function" )
def imdb():
    return IMDb( "fake-key" )


@pytest.fixture( scope="function" )
def mock_404_response():
    return Mock(
        spec=Response,
        status_code=404,
    )


@pytest.fixture( scope="function" )
def mock_ok_search( response_data ):
    good_search = response_data.get( "GOOD_SEARCH", {} )
    mock_json = Mock( return_value=good_search )
    return good_search, Mock(
        spec=Response,
        status_code=200,
        json=mock_json,
    )


def test_connection_error_when_offline( imdb ):
    functions = [ "search_titles", "movie_reviews", "movie_ratings" ]
    match = "Max retries exceeded with url"
    with pytest.raises( ConnectionError, match=match ):
        for function in functions:
            getattr( imdb, function ).__call__( "" )


def test_unfound_search_returns_nothing( imdb, mock_404_response ):
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_404_response ) as mock_get:
        assert imdb.search_titles( "" ) == {}


def test_ok_search( imdb, mock_ok_search ):
    mock_search, mock_response = mock_ok_search
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_response ) as mock_get:
        assert imdb.search_titles( "ok search" ) == mock_search


def test_unfound_review_returns_nothing( imdb, mock_404_response ):
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_404_response ) as mock_get:
        assert imdb.movie_reviews( "" ) == {}
