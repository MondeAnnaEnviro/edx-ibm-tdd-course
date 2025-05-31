package za.co.anna.monde.stack;

import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

class StackTest {

    @Test
    public void stackIsEmptyByDefault(){
        assertTrue( new Stack().isEmpty() );
    }
}
