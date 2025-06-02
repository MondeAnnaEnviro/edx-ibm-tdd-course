from typing import Any
from typing import Self
import pytest


class Queue:

    def __init__( self ):
        self.array = []

    def enqueue( self, value : Any ) -> Self:
        self.array.append( value )
        return self

    def dequeue( self ) -> Any:
        if self.array:
            return self.array.pop( 0 )

    def is_empty( self ) -> bool:
        return self.size() == 0

    def peek( self ) -> Any | None:
        if self.array:
            return self.array[ 0 ]

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
    queue.enqueue( "Item" )
    assert queue.size() == 1
    assert not queue.is_empty()
    assert queue.peek() == "Item"


def test_enqueue_of_two_items( queue ):
    queue.enqueue( "first" ).enqueue( "second" )
    assert queue.size() == 2
    assert not queue.is_empty()
    assert queue.peek() == "first"


def test_enqueue_of_multiple_items( queue ):
    queue.enqueue( 0 ).enqueue( 1 ).enqueue( 2 ).enqueue( 3 )
    assert queue.size() == 4
    assert not queue.is_empty()
    assert queue.peek() == 0


def test_dequeue_empty_queue( queue ):
    assert queue.dequeue() == None


def test_dequeue_when_one_item_present( queue ):
    queue.enqueue( "single" )
    assert queue.dequeue() == "single"
    assert queue.is_empty()
