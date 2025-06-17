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
    return IMDb()


@pytest.fixture( scope="function" )
def mock_404_response():
    return Mock(
        spec=Response,
        status_code=404,
    )


@pytest.fixture( scope="function" )
def mock_valid_response( response_data ):
    valid = response_data[ "VALID_RESPONSE" ]
    mock_json = Mock( return_value=valid )
    return valid, Mock(
        spec=Response,
        status_code=200,
        json=mock_json,
    )


@pytest.fixture( scope="function" )
def mock_invalid_response( response_data ):
    invalid = response_data[ "INVALID_RESPONSE" ]
    mock_json = Mock( return_value=invalid )
    return invalid, Mock(
        spec=Response,
        status_code=200,
        json=mock_json,
    )


@pytest.fixture( scope="function" )
def mock_ok_review( response_data ):
    good_review = response_data.get( "GOOD_REVIEW" )
    mock_json = Mock( return_value=good_review )
    return good_review, Mock(
        spec=Response,
        status_code=200,
        json=mock_json,
    )


@pytest.fixture( scope="function" )
def mock_ok_rating( response_data ):
    good_rating = response_data.get( "GOOD_RATING" )
    mock_json = Mock( return_value=good_rating )
    return good_rating, Mock(
        spec=Response,
        status_code=200,
        json=mock_json,
    )


@pytest.mark.skip( "w.i.p: url changed, expectation to be altered" )
def test_connection_error_when_offline( imdb ):
    functions = [ "search_titles", "movie_reviews", "movie_ratings" ]
    match = "Max retries exceeded with url"
    with pytest.raises( ConnectionError, match=match ):
        for function in functions:
            getattr( imdb, function ).__call__( "" )


def test_invalid_title_search( imdb, mock_invalid_response ):
    mock_invalid, mock_response = mock_invalid_response
    target = "models.imdb.requests.get"
    title = "pneumonoultramicroscopicvolcanoconiosis"

    with patch( target, return_value=mock_response ) as mock_get:
        results = imdb.search_titles( title )

        assert not len( results )
        assert results == mock_invalid


def test_valid_title_search( imdb, mock_valid_response ):
    mock_valid, mock_response = mock_valid_response
    mock_titles = mock_valid[ "titles" ]

    target = "models.imdb.requests.get"
    title = "Bambi"

    with patch( target, return_value=mock_response ) as mock_get:
        results = imdb.search_titles( title )

        assert len( results )
        assert results == mock_titles

        for result in results:
            assert title in result.get( "primary_title", "" )


@pytest.mark.skip( "w.i.p: url changed, expectation to be altered" )
def test_unfound_review_returns_nothing( imdb, mock_404_response ):
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_404_response ) as mock_get:
        assert imdb.movie_reviews( "" ) == {}


@pytest.mark.skip( "w.i.p: url changed, expectation to be altered" )
def test_ok_reviews( imdb, mock_ok_review ):
    mock_review, mock_response = mock_ok_review
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_response ) as mock_get:
        assert imdb.movie_reviews( "ok reviews" ) == mock_review


@pytest.mark.skip( "w.i.p: url changed, expectation to be altered" )
def test_unfound_rating_returns_nothing( imdb, mock_404_response ):
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_404_response ) as mock_get:
        assert imdb.movie_ratings( "" ) == {}


@pytest.mark.skip( "w.i.p: url changed, expectation to be altered" )
def test_ok_ratings( imdb, mock_ok_rating ):
    mock_rating, mock_response = mock_ok_rating
    target = "models.imdb.requests.get"
    with patch( target, return_value=mock_response ) as mock_get:
        assert imdb.movie_ratings( "ok ratings" ) == mock_rating
