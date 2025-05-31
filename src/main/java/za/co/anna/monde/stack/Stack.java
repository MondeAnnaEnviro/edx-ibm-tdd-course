package za.co.anna.monde.stack;

import java.util.ArrayList;
import java.util.List;

class Stack {

    private List<Integer> entries = new ArrayList<>();

    public boolean isEmpty(){
        return entries.isEmpty();
    }

    public Stack push( int integer ){
        entries.add( integer );
        return this;
    }

    public int size(){
        return entries.size();
    }
}
