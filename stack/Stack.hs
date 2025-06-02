module Stack where


data Stack a = Stack [ a ] deriving ( Show, Eq )


empty :: Stack a
empty = Stack []


isEmpty :: Stack a -> Bool
isEmpty ( Stack x ) = null x


peek :: Stack a -> a
peek ( Stack x ) = head x


push :: a -> Stack a -> Stack a
push x ( Stack xs ) = Stack ( x:xs )


size :: Stack a -> Int
size ( Stack x ) = length x
