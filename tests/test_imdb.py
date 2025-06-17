"""Test Cases for Mocking Lab"""
from requests.exceptions import ConnectionError
from requests import Response
from unittest.mock import patch, Mock
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
        json={},
    )


def test_connection_error_when_offline( imdb ):
    match = "Max retries exceeded with url"
    with pytest.raises( ConnectionError, match=match ):
        imdb.search_titles( "" )



def test_unfound_search_returns_nothing( imdb, mock_404_response ):
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_404_response ) as mock_get:
        assert imdb.search_titles( "" ) == {}
