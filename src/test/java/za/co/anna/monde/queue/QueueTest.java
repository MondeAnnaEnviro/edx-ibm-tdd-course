package za.co.anna.monde.queue;

import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class QueueTest {

    private Queue queue;

    @BeforeEach
    public void setUp(){
        queue = new Queue();
    }

    @Test
    public void anEmptyQueueIsSizeZero(){
        assertThat( queue.size() ).isEqualTo( 0 );
    }

    @Test
    public void aQueueWithSingleElementIsSizeOne(){
        Queue queue = new Queue( 1 );
        assertThat( queue.size() ).isEqualTo( 1 );
    }

    @Test
    public void aMultiElementQueueIsSizeN(){
        Queue queue = new Queue( new int[]{ 0, 1, 2, 3, 4 });
        assertThat( queue.size() ).isEqualTo( 5 );
    }
}
