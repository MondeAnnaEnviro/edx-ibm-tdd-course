from typing import Any
from typing import Self
import pytest


class Queue:

    def __init__( self ):
        self.array = []

    def is_empty( self ) -> bool:
        return self.size() == 0

    def peek( self ) -> Any | None:
        if self.array:
            return self.array[ 0 ]

    def push( self, value : Any ) -> Self:
        self.array.append( value )
        return self

    def size( self ) -> int:
        return len( self.array )


@pytest.fixture
def queue():
    yield Queue()


def test_queue_emptyness( queue ):
    assert queue.size() == 0
    assert queue.is_empty()
    assert queue.peek() == None


def test_enqueue_of_one_item( queue ):
    queue.push( "Item" )
    assert queue.size() == 1
    assert not queue.is_empty()
    assert queue.peek() == "Item"


def test_enqueue_of_two_items( queue ):
    queue.push( "first" ).push( "second" )
    assert queue.size() == 2
    assert not queue.is_empty()
    assert queue.peek() == "first"
