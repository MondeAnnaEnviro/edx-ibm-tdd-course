"""

"""

class Stack:

    def empty( self ):
        return True

    def push( self, datum ):
        return self

    def size( self ):
        return 1

    def peek( self ):
        return 2

    def pop( self ):
        raise RuntimeError( "cannot pop empty stack" )
