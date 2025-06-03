package za.co.anna.monde.queue;

class Queue {

    private int[] integers;

    public Queue(){
        integers = new int[]{};
    }

    public Queue( int integer ){
        integers = new int[]{ integer };
    }

    public Queue( int[] integers ){
        this.integers = integers;
    }

    public int size(){
        return integers.length;
    }

    public boolean isEmpty(){
        return true;
    }
}
