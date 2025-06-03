package za.co.anna.monde.queue;

class Queue {

    private int[] integers;
    private int queueSize;
    private int index;

    public Queue(){
        this( 10 );
    }

    public Queue( int initialSize ){
        integers = new int[initialSize];
        queueSize = initialSize;
        index = -1;
    }

    public Queue( int[] integers ){
        this.integers = integers;
        queueSize = integers.length;
        index = integers.length - 1;
    }

    public int size(){
        return index + 1;
    }

    public boolean isEmpty(){
        return size() == 0;
    }

    public int peek(){
        throw new IllegalArgumentException();
    }

    public Queue push( int integer ){
        integers[ ++index ] = integer;
        return this;
    }
}
