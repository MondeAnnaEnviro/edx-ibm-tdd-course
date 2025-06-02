from typing import Any
import pytest


class Queue:

    def __init__( self ):
        self.array = []

    def is_empty( self ) -> bool:
        return self.size() == 0

    def peek( self ) -> Any | None:
        if self.array:
            return self.array[ -1 ]

    def push( self, value : Any ) -> None:
        self.array.append( value )

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
