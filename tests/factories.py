"""
AccountFactory class using FactoryBoy

Documentation on Faker Providers:
    https://faker.readthedocs.io/en/master/providers/baseprovider.html

Documentation on Fuzzy Attributes:
    https://factoryboy.readthedocs.io/en/stable/fuzzy.html

"""
from factory.fuzzy import FuzzyChoice, FuzzyDate
from factory import Factory, Faker, Sequence
from datetime import date


from models.account import Account


class AccountFactory( Factory ):
    """ Creates fake Accounts """

    class Meta:
        model = Account

    _id = Sequence( lambda x: x )
    name = Faker( "name" )
    email = Faker( "email" )
    phone_number = Faker( "phone_number" )
    disabled = FuzzyChoice( choices=[ "True", "False" ])
    date_joined = FuzzyDate( date( 2000, 1, 1 ))
