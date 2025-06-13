"""
Test Cases TestAccountModel
"""

from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest.mock import patch
from unittest import mock
from pathlib import Path
import datetime
import pytest
import json


from models.account import Account
from models import app


@pytest.fixture( scope="session" )
def mock_session( data_in_account_format ):
    data = [
        ([ mock.call.query( Account ), mock.call.filter( Account.id == _id )],[ account ])
        for _id, account
        in enumerate( data_in_account_format, start=1 )
    ]

    _mock_session = UnifiedAlchemyMagicMock( data=data )

    yield _mock_session

    _mock_session.rollback()
    _mock_session.close()


@pytest.fixture( scope="session" )
def data_in_dict_format():
    """Loads JSON data from a file."""
    fixture_path = "/tests/fixtures/account_data.json"
    file_path = str( Path.cwd() ) + fixture_path

    with Path( file_path ).open() as file:
        return json.load( file )


@pytest.fixture( scope="session" )
def data_in_account_format( data_in_dict_format ):
    return [
        Account( id=_id, **account, date_joined=datetime.datetime.now() )
        for _id, account
        in enumerate( data_in_dict_format, start=1 )
    ]


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


def test_querying_all_when_session_has_data_returns_all_data( app_context, data_in_dict_format ):
    with patch( "models.account.Account.query" ) as mock_query:
        mock_query.all.return_value = data_in_dict_format
        result = Account.all()

        mock_query.all.assert_called_once()
        assert result == data_in_dict_format


def test_calling_find_using_invalid_id( app_context ):
    target = "models.account.Account.query.session.query"

    with patch( target ) as mock_query:
        mock_query.return_value.filter.return_value.first.return_value = None

        result = Account.find( 111 )
        assert result is None

        mock_query.return_value.filter.return_value.first.assert_called_once()


def test_calling_find_using_valid_id( app_context, mock_session, data_in_account_format ):
    target = "models.account.Account.query"

    with patch( target ) as mock_query:
        mock_query.session = mock_session

        for _id, account in enumerate( data_in_account_format, start=1 ):
            result = Account.find( _id )

            assert result == account
            mock_session.query.return_value.filter.return_value.first.assert_called()
