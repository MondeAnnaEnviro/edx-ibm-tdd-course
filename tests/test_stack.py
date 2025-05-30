import pytest
from stack.stack import Stack


def test_new_stack_is_empty():
    assert Stack().empty()


def test_push_increases_size_by_one():
    assert Stack().push( 100 ).size() == 1


def test_last_push_is_on_top():
    assert Stack().push( 1 ).push( 2 ).peek() == 2


def test_popping_empty_stack_raises_error():
    match = "cannot pop empty stack"
    with pytest.raises( RuntimeError, match=match ):
        Stack().pop()
