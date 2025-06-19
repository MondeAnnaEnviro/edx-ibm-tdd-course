"""Test Cases for Mocking Lab"""
from requests.exceptions import ConnectionError
from requests import Response
from unittest.mock import patch, Mock
from pathlib import Path
import pytest
import json


from fixtures import pickler
from models import IMDb


@pytest.fixture( scope="function" )
def imdb():
    return IMDb()


@pytest.fixture( scope="function" )
def mock_bad_request_response():
    return pickler.unpickle_response( "bad_request_response" )


@pytest.fixture( scope="function" )
def mock_valid_title_search_response():
    return pickler.unpickle_response( "valid_title_search_response" )


@pytest.fixture( scope="function" )
def mock_invalid_title_search_response():
    return pickler.unpickle_response( "invalid_title_search_response" )


@pytest.fixture( scope="function" )
def mock_valid_imdb_id_response():
    return pickler.unpickle_response( "valid_imdb_id_response" )


@pytest.fixture( scope="function" )
def mock_invalid_imdb_id_response():
    return pickler.unpickle_response( "invalid_imdb_id_response" )


@pytest.fixture( scope="function" )
def mock_valid_webscrapping_response():
    return pickler.unpickle_response( "valid_webscrapping_response" )


@pytest.mark.skip( "w.i.p: url changed, expectation to be altered" )
def test_connection_error_when_offline( imdb ):
    functions = [ "search_titles", "movie_reviews", "movie_ratings" ]
    match = "Max retries exceeded with url"
    with pytest.raises( ConnectionError, match=match ):
        for function in functions:
            getattr( imdb, function ).__call__( "_invalid_input_" )


def test_bad_request_for_title_search( imdb, mock_bad_request_response ):
    target = "models.imdb.requests.get"
    title = ""
    with patch( target, return_value=mock_bad_request_response ) as mock_get:
        results = imdb.search_titles( title )
        assert results == []


def test_invalid_title_search( imdb, mock_invalid_title_search_response ):
    target = "models.imdb.requests.get"
    title = "pneumonoultramicroscopicvolcanoconiosis"
    with patch( target, return_value=mock_invalid_title_search_response ) as mock_get:
        results = imdb.search_titles( title )
        assert results == []


def test_valid_title_search( imdb, mock_valid_title_search_response ):
    target = "models.imdb.requests.get"
    title = "Bambi"

    with patch( target, return_value=mock_valid_title_search_response ) as mock_get:
        results = imdb.search_titles( title )

        assert len( results )

        for result in results:
            assert title in result.get( "primary_title", "" )


def test_invalid_reviews( imdb, mock_invalid_imdb_id_response ):
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_invalid_imdb_id_response ) as mock_get:
        assert imdb.movie_reviews( "tt-INVALID_ID" ) == { "reviews": [] }


def test_valid_reviews( imdb, mock_valid_imdb_id_response, mock_valid_title_search_response, mock_valid_webscrapping_response ):
    valid_id = mock_valid_imdb_id_response.json()[ "id" ]
    target = "models.imdb.requests.get"

    imdb.search_titles = Mock( return_value=mock_valid_title_search_response.json().get( "titles" ))
    imdb._is_valid_imdb_id = Mock( return_value=[ True, "misc" ])

    with patch( target, return_value=mock_valid_webscrapping_response ) as mock_get:
        result = imdb.movie_reviews( valid_id )
        reviews = result[ "reviews" ]

        assert "Whatever Kleenex moments it causes, Bambi is unmissable." in reviews
        assert "From Disney's richest period, interleaving splendid animation with vulgar Americana. " in reviews


def test_invalid_rating( imdb, mock_invalid_imdb_id_response ):
    target = "models.imdb.requests.get"

    with patch( target, return_value=mock_invalid_imdb_id_response ) as mock_get:
        results = imdb.movie_ratings( "tt-INVALID_ID" )

        assert len( results )
        assert results ==  {
            "id": None,
            "primary_title": None,
            "rating": None,
        }


def test_valid_rating( imdb, mock_valid_imdb_id_response ):
    target = "models.imdb.requests.get"
    imdb_id = "tt3205278"

    with patch( target, return_value=mock_valid_imdb_id_response ) as mock_get:
        results = imdb.movie_ratings( imdb_id )

        assert len( results )
        assert results == {
            "id":               "tt3205278",
            "primary_title":    "Bambi Cottages",
            "rating":           { "aggregate_rating": 8.2, "votes_count": 12 },
        }
