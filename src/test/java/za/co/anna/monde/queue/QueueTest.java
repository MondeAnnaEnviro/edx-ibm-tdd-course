package za.co.anna.monde.queue;

import static org.assertj.core.api.Assertions.assertThatIllegalArgumentException;
import static org.assertj.core.api.Assertions.assertThatRuntimeException;
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
    public void anNewQueueIsSizeZero(){
        assertThat( queue.size() ).isEqualTo( 0 );
    }

    @Test
    public void aQueueWithSingleElementIsSizeOne(){
        queue = new Queue( 1 ).enqueue( 22 );
        assertThat( queue.size() ).isEqualTo( 1 );
    }

    @Test
    public void aMultiElementQueueIsSizeN(){
        Queue queue = new Queue( new int[]{ 0, 1, 2, 3, 4 });
        assertThat( queue.size() ).isEqualTo( 5 );
    }

    @Test
    public void aNewQueueIsEmpty(){
        assertThat( queue.isEmpty() ).isTrue();
    }

    @Test
    public void aPopulatedQueueIsNotEmpty(){
        assertThat( new Queue().enqueue( 0 ).isEmpty() ).isFalse();
        assertThat( new Queue( new int[]{ 0 }).isEmpty() ).isFalse();
    }

    @Test
    public void peekingAnEmptyQueueRaisesError(){
        assertThatIllegalArgumentException().isThrownBy(
            () -> queue.peek()
        );
    }

    @Test
    public void peekingWhereThereIsOneElementShowsSaidElement(){
        assertThat( queue.enqueue( 77 ).peek() ).isEqualTo( 77 );
    }

    @Test
    public void peekingMultipleElementsShowsFirstElement(){
        assertThat(
            queue.enqueue( 0 ).enqueue( 1 ).enqueue( 2 ).peek()
        ).isEqualTo( 0 );
    }

    @Test
    public void enqueueOnce(){
        queue.enqueue( 0 );
        assertThat( queue.size() ).isEqualTo( 1 );
        assertThat( queue.peek() ).isEqualTo( 0 );
        assertThat( queue.isEmpty() ).isFalse();
    }

    @Test
    public void enqueueTwice(){
        queue.enqueue( 10 ).enqueue( 20 );
        assertThat( queue.size() ).isEqualTo( 2 );
        assertThat( queue.peek() ).isEqualTo( 10 );
        assertThat( queue.isEmpty() ).isFalse();
    }

    @Test
    public void enqueueMultipleTimes(){
        queue.enqueue( -1 ).enqueue( -2 ).enqueue( -3 ).enqueue( -4 );
        assertThat( queue.size() ).isEqualTo( 4 );
        assertThat( queue.peek() ).isEqualTo( -1 );
        assertThat( queue.isEmpty() ).isFalse();
    }

    @Test
    public void enqueueMoreThanInitialSizeOfQueue(){
        queue = new Queue( new int[]{ 0, 1, 2 }).enqueue( 3 );
        assertThat( queue.size() ).isEqualTo( 4 );
        assertThat( queue.peek() ).isEqualTo( 0 );
        assertThat( queue.isEmpty() ).isFalse();
    }

    @Test
    public void dequeueOfEmptyQueueThrows(){
        assertThatRuntimeException().isThrownBy(
            () -> queue.dequeue()
        );
    }

    @Test
    public void dequeueOfSingleElementReturnsSaidElement(){
        int dequeued = queue.enqueue( 5 ).dequeue();

        assertThat( dequeued ).isEqualTo( 5 );
        assertThat( queue.size() ).isEqualTo( 0 );
        assertThat( queue.isEmpty() ).isTrue();
    }
}
