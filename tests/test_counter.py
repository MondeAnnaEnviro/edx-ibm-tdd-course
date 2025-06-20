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
