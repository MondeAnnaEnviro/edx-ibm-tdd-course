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

        return not len( self )

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

    def peek( self ):
        """
        Informs caller of item at top of stack
        at time of call

        Return
        ======
        type:           Any
        description:    The last pushed item
        """

        self.validate_operability( "peek" )
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

        self.validate_operability( "pop" )
        return self._DATA.pop()

    def validate_operability( self, operation ):
        if self.empty():
            raise RuntimeError(
                f"cannot { operation } empty stack"
            )

    def __len__( self ):
        """
        Assissts the length dunder function in
        determining the size of the stack

        Return
        ======
        type:           int
        description:    Positive count of stack's
                        items
        """

        return len( self._DATA )
