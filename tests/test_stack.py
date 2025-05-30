
from stack.stack import Stack


def test_new_stack_is_empty():
    assert Stack().empty()


def test_pushing_once_increases_size_by_one():
    assert Stack().push( 100 ).size() == 1
