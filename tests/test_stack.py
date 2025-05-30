from stack.stack import Stack
import pytest


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


def test_pop_returns_last_pushed_item():
    assert Stack().push( 77 ).pop() == 77


def test_n_pushes_and_n_pops_render_empty_stack():
    stack = Stack().push( 83 ).push( 4544 )
    stack.pop()
    stack.pop()
    assert stack.empty()
