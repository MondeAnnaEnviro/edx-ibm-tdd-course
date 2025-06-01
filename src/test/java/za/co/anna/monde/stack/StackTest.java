package za.co.anna.monde.stack;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class StackTest {

    private Stack stack;

    @BeforeEach
    public void setUp(){
        stack = new Stack();
    }

    @Test
    public void stackIsEmptyByDefault(){
        assertTrue( stack.isEmpty() );
    }

    @Test
    public void stackIsNotEmptyWhenItemAdded(){
        assertFalse( stack.push( 0 ).isEmpty() );
    }

    @Test
    public void anEmptyStackHasSizeOfZero(){
        assertEquals( 0, stack.size() );
    }

    @Test
    public void firstPushIncreasesSizeToOne(){
        assertEquals( 1, stack.push( 10 ).size() );
    }

    @Test
    public void afterNthPushStackIsSizeN(){
        assertEquals( 2, stack.push( 1 ).push( 2 ).size() );
    }

    @Test
    public void peekingEmptyStackThrowsException(){
        Exception exception = assertThrows(
                IllegalStateException.class,
                () -> stack.peek()
        );

        assertEquals( "unable to peek at empty stack", exception.getMessage() );
    }

    @Test
    public void peekingAtPopulatedStackProvidesLastEntry(){
        assertEquals( 33, stack.push( 3 ).push( 0 ).push( 33 ).peek() );
    }

    @Test
    public void poppingEmptyStackThrowsException(){
        Exception exception = assertThrows(
                IllegalStateException.class,
                () -> stack.pop()
        );

        assertEquals( "unable to pop from empty stack", exception.getMessage() );
    }

    @Test
    public void poppingAtPopulatedStackRemovesAndReturnsLastEntry(){
        stack.push( 52 ).push( 184 ).push( -2 );
        assertEquals( -2, stack.pop() );
        assertEquals( 184, stack.pop() );
        assertEquals( 52, stack.pop() );
    }

    @Test
    public void multiOperationalProcessing(){
        assertEquals(  1, stack.push( 23 ).size() );
        assertEquals( 33, stack.push( 15 ).push( 33 ).peek() );
        assertEquals( 33, stack.pop() );
    }
}
