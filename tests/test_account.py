"""
Test Cases TestAccountModel
"""

from unittest.mock import patch
from pathlib import Path
import pytest
import json


from models.account import Account
from models import app


@pytest.fixture( scope="session" )
def account_data():
    """Loads JSON data from a file."""
    fixture_path = "/tests/fixtures/account_data.json"
    file_path = str( Path.cwd() ) + fixture_path

    with Path( file_path ).open() as file:
        return json.load( file )


@pytest.fixture( scope="session" )
def app_context():
    with app.app_context():
        yield


def test_querying_all_when_session_is_empty_returns_empty_list( app_context ):
    with patch( "models.account.Account.query" ) as mock_query:
        mock_query.all.return_value = []
        result = Account.all()

        mock_query.all.assert_called_once()
        assert result == []


def test_querying_all_when_session_has_data_returns_all_data( app_context, account_data ):
    with patch( "models.account.Account.query" ) as mock_query:
        mock_query.all.return_value = account_data
        result = Account.all()

        mock_query.all.assert_called_once()
        assert result == account_data
