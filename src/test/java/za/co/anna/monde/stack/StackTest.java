package za.co.anna.monde.stack;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
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
    public void firstPushIncreasesSizeToOne(){
        assertEquals( 1, new Stack().push( 10 ).size() );
    }
}
