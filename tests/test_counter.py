"""
Test Cases for Counter Web Service
"""
import pytest
from unittest import TestCase


from counter import counter, status


@pytest.fixture
def client():
    return counter.app.test_client()


def test_creating_new_counter( client ):
    """It should create a counter"""
    response = client.post( "/counters/item" )
    data = response.get_json()

    assert response.status_code == status.HTTP_201_CREATED
    assert data[ "item" ] == 0


@pytest.mark.skip
def test_creating_duplicate_counter( client ):
    """It should return an error for duplicates"""
    first_response = client.post( "/counters/item" )
    second_response = client.post( "/counters/item" )

    assert first_response == status.HTTP_201_CREATED
    assert second_response == status.HTTP_409_CONFLICT
