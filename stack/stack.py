"""

"""

class Stack:

    def __init__( self ):
        self._DATA = []

    def empty( self ):
        return not self.size()

    def push( self, datum ):
        self._DATA.append( datum )
        return self

    def size( self ):
        return len( self._DATA )

    def peek( self ):
        return self._DATA[ -1 ]

    def pop( self ):
        if self.empty():
            raise RuntimeError( "cannot pop empty stack" )
        return self._DATA.pop()
