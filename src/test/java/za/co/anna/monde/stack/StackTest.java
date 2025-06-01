package za.co.anna.monde.stack;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

class StackTest {

    @Test
    public void stackIsEmptyByDefault(){
        assertTrue( new Stack().isEmpty() );
    }

    @Test
    public void stackIsNotEmptyWhenItemAdded(){
        assertFalse( new Stack().push( 0 ).isEmpty() );
    }

    @Test
    public void anEmptyStackHasSizeOfZero(){
        assertEquals( 0, new Stack().size() );
    }

    @Test
    public void firstPushIncreasesSizeToOne(){
        assertEquals( 1, new Stack().push( 10 ).size() );
    }

    @Test
    public void afterNthPushStackIsSizeN(){
        assertEquals( 2, new Stack().push( 1 ).push( 2 ).size() );
    }

    @Test
    public void peekingEmptyStackThrowsException(){
        Exception exception = assertThrows(
                IllegalStateException.class,
                () -> new Stack().peek()
        );

        assertEquals( "unable to peek at empty stack", exception.getMessage() );
    }

    @Test
    public void peekingAtPopulatedStackProvidesLastEntry(){
        assertEquals( 33, new Stack().push( 3 ).push( 0 ).push( 33 ).peek() );
    }

    @Test
    public void poppingEmptyStackThrowsException(){
        Exception exception = assertThrows(
                IllegalStateException.class,
                () -> new Stack().pop()
        );

        assertEquals( "unable to pop from empty stack", exception.getMessage() );
    }

    @Test
    public void poppingAtPopulatedStackRemovesAndReturnsLastEntry(){
        Stack stack = new Stack().push( 52 ).push( 184 ).push( -2 );
        assertEquals( -2, stack.pop() );
        assertEquals( 184, stack.pop() );
        assertEquals( 52, stack.pop() );
    }

    @Test
    public void multiOperationalProcessing(){
        Stack stack = new Stack().push( 23 );
        assertEquals( 1, stack.size() );
        assertEquals( 33, stack.push( 15 ).push( 33 ).peek() );
        assertEquals( 33, stack.pop() );
    }
}
