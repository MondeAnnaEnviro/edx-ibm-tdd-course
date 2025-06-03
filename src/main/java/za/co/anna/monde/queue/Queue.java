package za.co.anna.monde.queue;

class Queue {

    private int[] integers;

    public Queue(){
        integers = new int[]{};
    }

    public Queue( int integer ){
        integers = new int[]{ integer };
    }

    public int size(){
        return integers.length;
    }
}
