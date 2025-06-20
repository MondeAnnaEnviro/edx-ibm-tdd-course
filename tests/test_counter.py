"""
Test Cases for Counter Web Service
"""
import pytest
from unittest import TestCase


from counter import counter, status


@pytest.fixture( scope="function" )
def client():
    yield counter.create_app().test_client()


def test_creating_new_counter( client ):
    """It should create a counter"""
    response = client.post( "/counters/item" )
    data = response.get_json()

    assert response.status_code == status.HTTP_201_CREATED
    assert data[ "item" ] == 0


def test_creating_duplicate_counter( client ):
    """It should return an error for duplicates"""
    first_response = client.post( "/counters/item" )
    second_response = client.post( "/counters/item" )

    assert first_response.status_code == status.HTTP_201_CREATED
    assert second_response.status_code == status.HTTP_409_CONFLICT


def test_deleting_when_no_counter_exists( client ):
    """It should return no content status"""
    response = client.delete( "/counters/item" )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_deleting_newly_created_counter( client ):
    """It should return no content message after delete"""
    client.post( "/counters/item" )

    response = client.delete( "counters/item" )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_deleting_updated_counter( client ):
    """It should return no content message after delete"""
    client.post( "/counters/item" )
    client.put( "/counters/item" )

    response = client.delete( "counters/item" )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_reading_when_no_counter_exists( client ):
    """It should return no content status"""
    response =  client.get( "/counters/item" )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_reading_newly_created_counter( client ):
    """It should return a count of zero"""
    client.post( "/counters/item" )

    response = client.get( "counters/item" )
    data = response.get_json()

    assert response.status_code == status.HTTP_200_OK
    assert data[ "item" ] == 0


def test_reading_singley_updated_counter( client ):
    """It should return a count of one"""
    client.post( "/counters/item" )
    client.put( "/counters/item" )

    response = client.get( "counters/item" )
    data = response.get_json()

    assert response.status_code == status.HTTP_200_OK
    assert data[ "item" ] == 1


def test_reading_with_multiple_updates( client ):
    """It should return a count of one"""
    client.post( "/counters/item" )

    num_calls = 10

    for _ in range( num_calls ):
        client.put( "/counters/item" )

    response = client.get( "counters/item" )
    data = response.get_json()

    assert response.status_code == status.HTTP_200_OK
    assert data[ "item" ] == num_calls


def test_updating_when_no_counter_exists( client ):
    """It should return no content status"""
    response = client.put( "/counters/item" )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_updating_a_counter( client ):
    """It should update a counter"""
    client.post( "/counters/item" )

    response = client.put( "/counters/item" )
    data = response.get_json()

    assert response.status_code == status.HTTP_200_OK
    assert data[ "item" ] == 1


def test_updating_counter_multiple_times( client ):
    """It should update a counter"""
    client.post( "/counters/item" )

    num_calls = 10

    for _ in range( num_calls ):
        response = client.put( "/counters/item" )

    data = response.get_json()

    assert response.status_code == status.HTTP_200_OK
    assert data[ "item" ] == num_calls
