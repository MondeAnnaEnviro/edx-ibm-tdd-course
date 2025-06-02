import pytest


class Queue:

    def is_empty( self ) -> bool:
        return True

    def peek( self ) -> None:
        ...

    def size( self ) -> int:
        return 0


@pytest.fixture
def queue():
    yield Queue()


def test_queue_emptyness( queue ):
    assert queue.size() == 0
    assert queue.is_empty()
    assert queue.peek() == None
