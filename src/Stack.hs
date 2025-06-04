module Stack ( Stack, empty, isEmpty, peek, pop, push, size ) where


newtype Stack a = Stack [ a ] deriving ( Show, Eq )


empty :: Stack a
empty = Stack []


isEmpty :: Stack a -> Bool
isEmpty ( Stack x ) = null x


peek :: Stack a -> Maybe a
peek ( Stack [] ) = Nothing
peek ( Stack x ) = Just $ head x


pop :: Stack a -> ( Maybe a, Stack a )
pop ( Stack [] ) = ( Nothing, Stack [] )
pop ( Stack ( x:xs )) = ( Just x, Stack xs )


push :: a -> Stack a -> Stack a
push x ( Stack xs ) = Stack ( x:xs )


size :: Stack a -> Int
size ( Stack x ) = length x
