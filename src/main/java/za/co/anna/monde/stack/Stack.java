package za.co.anna.monde.stack;

import java.util.List;

class Stack {

    private boolean isEmpty = true;

    public boolean isEmpty(){
        return isEmpty;
    }

    public Stack push( int integer ){
        isEmpty = false;
        return this;
    }

    public int size(){
        return 1;
    }
}
