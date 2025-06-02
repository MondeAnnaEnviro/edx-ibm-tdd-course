module Stack where


data Stack a = Stack [ a ] deriving ( Show, Eq )


isEmpty :: Stack a -> Bool
isEmpty ( Stack x ) = null x


peek :: Stack a -> a
peek ( Stack x ) = head x


size :: Stack a -> Int
size ( Stack x ) = length x


push :: a -> Stack a -> Stack a
push x ( Stack xs ) = Stack ( x:xs )
