package za.co.anna.monde.queue;

class Queue {

    private final int BASE_SIZE = 10;
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

    public int dequeue(){
        throw new RuntimeException();
    }

    public Queue enqueue( int integer ){
        if ( index + 1 == queueSize )
            integers = increaseIntegers( integers );
        integers[ ++index ] = integer;
        return this;
    }

    public boolean isEmpty(){
        return size() == 0;
    }

    public int peek(){
        if ( index < 0 )
            throw new IllegalArgumentException();

        return integers[ 0 ];
    }

    public int size(){
        return index + 1;
    }

    private int[] increaseIntegers( int[] integers ){
        int[] newIntegers = new int[ integers.length + BASE_SIZE ];

        for ( int iter = 0; iter < integers.length; iter++ )
            newIntegers[ iter ] = integers[ iter ];
        return newIntegers;
    }
}
