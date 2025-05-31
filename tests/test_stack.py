from stack.stack import Stack
import pytest


@pytest.fixture( scope="function" )
def stack():
    yield Stack()


@pytest.fixture( scope="function" )
def filled_stack():
    stack = Stack()
    stack._DATA = [ 1, 3, 5, 7 ]
    yield stack


def test_new_stack_is_empty( stack ):
    assert stack.empty()


def test_push_increases_size_by_one( stack ):
    assert len( stack.push( 100 )) == 1


def test_stack_with_items_is_not_empty( filled_stack ):
    assert not filled_stack.empty()


def test_last_push_is_on_top( filled_stack ):
    assert filled_stack.peek() == 7


def test_peeking_empty_stack_raises_error( stack ):
    match = "cannot peek empty stack"
    with pytest.raises( RuntimeError, match=match ):
        Stack().peek()


def test_popping_empty_stack_raises_error( stack ):
    match = "cannot pop empty stack"
    with pytest.raises( RuntimeError, match=match ):
        stack.pop()


def test_pop_returns_last_pushed_item( filled_stack ):
    assert filled_stack.pop() == 7


def test_n_pushes_and_n_pops_render_empty_stack( stack ):
    stack.push( 83 )
    stack.pop()
    assert stack.empty()


def test_three_pushes_and_one_pop_leave_two_item( stack ):
    stack.push( 55 ).push( 45 ).push( 44 )
    stack.pop()
    assert len( stack ) == 2
    assert stack.peek() == 45
