package za.co.anna.monde.queue;

import static org.assertj.core.api.Assertions.assertThatIllegalArgumentException;
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
        queue = new Queue( 1 ).push( 22 );
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
        assertThat( new Queue().push( 0 ).isEmpty() ).isFalse();
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
        assertThat( queue.push( 77 ).peek() ).isEqualTo( 77 );
    }

    @Test
    public void peekingMultipleElementsShowsFirstElement(){
        assertThat( queue.push( 0 ).push( 1 ).push( 2 ).peek() ).isEqualTo( 0 );
    }

    @Test
    public void pushOnce(){
        queue.push( 0 );
        assertThat( queue.size() ).isEqualTo( 1 );
        assertThat( queue.peek() ).isEqualTo( 0 );
        assertThat( queue.isEmpty() ).isFalse();
    }

    @Test
    public void pushTwice(){
        queue.push( 10 ).push( 20 );
        assertThat( queue.size() ).isEqualTo( 2 );
        assertThat( queue.peek() ).isEqualTo( 10 );
        assertThat( queue.isEmpty() ).isFalse();
    }
}
