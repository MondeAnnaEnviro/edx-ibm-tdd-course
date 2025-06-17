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


def test_connection_error_when_offline( imdb ):
    match = "Max retries exceeded with url"
    with pytest.raises( ConnectionError, match=match ):
        imdb.search_titles( "" )

