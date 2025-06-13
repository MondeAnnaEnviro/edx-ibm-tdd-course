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
def app_context():
    with app.app_context():
        yield


@pytest.fixture( scope="session" )
def account_data():
    """Loads JSON data from a file."""
    fixture_path = "/tests/fixtures/account_data.json"
    file_path = str( Path.cwd() ) + fixture_path

    with Path( file_path ).open() as file:
        return json.load( file )


@pytest.fixture( scope="session" )
def accounts( account_data ):
    return [
        Account( _id=_id, **account, date_joined=datetime.datetime.now() )
        for _id, account
        in enumerate( account_data, start=1 )
    ]


@pytest.fixture( scope="session" )
def mock_session( app_context, accounts ):
    query_all = [(
        [ mock.call.query( Account ), mock.call.filter( Account._id > 0 )],
        accounts
    )]

    query_individual_accounts = [
        ([ mock.call.query( Account ), mock.call.filter( Account._id == _id )], [ account ])
        for _id, account
        in enumerate( accounts, start=1 )
    ]

    queries = query_all + query_individual_accounts

    _mock_session = UnifiedAlchemyMagicMock( data=queries )

    yield _mock_session

    _mock_session.rollback()
    _mock_session.close()


@pytest.fixture( scope="session" )
def mock_empty_session( app_context ):
    query = [([ mock.call.query( Account ), mock.call.filter( Account._id > 0 )], [] )]
    _mock_session = UnifiedAlchemyMagicMock( data=query )

    yield _mock_session

    _mock_session.rollback()
    _mock_session.close()


def test_querying_all_when_session_has_no_data( mock_empty_session ):
    with patch( "models.account.Account.query" ) as mock_query:
        mock_query.session = mock_empty_session
        result = Account.all()

        assert result == []
        mock_query.session.query.return_value   \
            .filter.return_value                \
            .all.assert_called_once()


def test_querying_all_when_session_has_data( mock_session, accounts ):
    with patch( "models.account.Account.query" ) as mock_query:
        mock_query.session = mock_session
        result = Account.all()

        assert result == accounts
        mock_query.session.query.return_value   \
            .filter.return_value                \
            .all.assert_called_once()


def test_calling_find_using_invalid_id( mock_session ):
    with patch( "models.account.Account.query" ) as mock_query:
        mock_query.session = mock_session
        result = Account.find( 111 )

        assert result is None
        mock_query.session.query.return_value   \
            .filter.return_value                \
            .first.assert_called_once()


def test_calling_find_using_valid_id( mock_session, accounts ):
    with patch( "models.account.Account.query" ) as mock_query:
        mock_query.session = mock_session

        for _id, account in enumerate( accounts, start=1 ):
            result = Account.find( _id )

            assert result == account
            mock_query.session.query.return_value   \
                .filter.return_value                \
                .first.assert_called()


def test_to_dict_for_populated_accounts( app_context, accounts, account_data ):
    for account, data in zip( accounts, account_data ):
        dict_ = account.to_dict()

        """
        - being able to pop the keys asserts their existence
        - likewise, the keys are created when saving accounts
        """
        dict_.pop( "_id" )
        dict_.pop( "date_joined" )

        assert dict_ == data

def test_to_dict_for_unpopulated_accounts( app_context ):
    assert Account().to_dict() == {
        "_id": None, "name": None, "email": None,
        "phone_number": None, "disabled": None,
        "date_joined": None
    }
