"""
Abastract Data Type: Stack
A last-in, last-out data structure
"""

class Stack:

    def __init__( self ):
        self._DATA = []

    def empty( self ):
        """
        Informs caller as to whether the stack has
        items in it or not

        Return
        ======
        type:           bool
        description:    True if not items present,
                        else False
        """

        return not self.size()

    def push( self, datum ):
        """
        Adds provided datum to the top of the stack

        Parameter
        =========
        datum:          datum to be added

        Return
        ======
        type:           Stack
        description:    The very same instance
        """

        self._DATA.append( datum )
        return self

    def size( self ):
        """
        Informs caller of the size of the stack
        at the time of call

        Return
        ======
        type:           int
        description:    Positive count of stack'
                        items
        """

        return len( self._DATA )

    def peek( self ):
        """
        Informs caller of item at top of stack
        at time of call

        Return
        ======
        type:           Any
        description:    The last pushed item
        """

        return self._DATA[ -1 ]

    def pop( self ):
        """
        Removes and returns the top most item
        in stack

        Return
        ======
        type:           Any
        description:    Removes and returns the
                        top most item in stack
        """

        if self.empty():
            raise RuntimeError( "cannot pop empty stack" )
        return self._DATA.pop()
