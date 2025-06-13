"""Account class"""
from typing_extensions import Self
from sqlalchemy.sql import func
from models import db
import logging


logger = logging.getLogger()


class DataValidationError( Exception ):
    """Used for an data validation errors when deserializing"""


class Account( db.Model ):
    """ Class that represents an Account """

    _id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 64 ))
    email = db.Column( db.String( 64 ))
    phone_number = db.Column( db.String( 32 ), nullable=True )
    disabled = db.Column( db.Boolean(), nullable=False, default=False )
    date_joined = db.Column( db.Date, nullable=False, server_default=func.now() )

    @classmethod
    def all( cls ) -> list:
        """Returns all of the Accounts in the database"""
        logger.info("Processing all Accounts")
        return cls.query.session.query( cls ).filter( cls._id > 0 ).all()

    @classmethod
    def find( cls, account_id: int ) -> int:
        """Finds an Account by it's ID
        :param account_id: the id of the Account to find
        :type account_id: int
        :return: an instance with the account_id, or None if not found
        :rtype: Account
        """
        logger.info( "Processing lookup for id {account_id} ..." )
        return cls.query.session.query( cls ).filter( cls._id == account_id ).first()

    @classmethod
    def from_dict( cls, data: dict ) -> Self:
        """Sets attributes from a dictionary"""
        return cls( **data )

    def to_dict( self ) -> dict:
        """Serializes the class as a dictionary"""
        return { c.name: getattr( self, c.name ) for c in self.__table__.columns }

    def save( self ):
        """Saves Account in the database"""
        logger.info( f"Saving {self.name}" )
        db.session.add( self )
        db.session.commit()

    def update( self ):
        """Updates an Account in the database"""
        logger.info( f"Updating {self.name}" )
        if not self._id:
            raise DataValidationError( "Update called with empty ID field" )

        saved = self.find( self._id )

        if saved is None:
            self.save()
        else:
            db.session.delete( saved )
            self.save()

    def delete(self):
        """Removes an Account from the database"""
        logger.info( f"Deleting {self.name}" )
        db.session.delete( self )
        db.session.commit()

    def __eq__( self, other ):
        return self._id == other._id                    and \
               self.name == other.name                  and \
               self.email == other.email                and \
               self.disabled == other.disabled          and \
               self.date_joined == other.date_joined    and \
               self.phone_number == other.phone_number

    def __repr__( self ):
        return f"<Account {self.name}>"
