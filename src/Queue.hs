module Queue ( Queue, empty, isEmpty, peek, pop, push, size ) where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


empty :: Queue a
empty = Queue []


isEmpty :: Queue a -> Bool
isEmpty ( Queue x ) = size ( Queue x ) == 0


peek :: Queue a -> Maybe a
peek ( Queue [] ) = Nothing
peek ( Queue ( x:xs ))
 | size ( Queue xs ) == 0 = Just x
 | otherwise = peek ( Queue xs )


pop :: Queue a -> ( Maybe a, Queue a )
pop ( Queue [] ) = ( Nothing, Queue [] )
pop ( Queue [ x ]) = ( Just x, Queue [] )


push :: a -> Queue a -> Queue a
push x ( Queue [] ) = Queue [ x ]
push x ( Queue xs ) = Queue ( x:xs)


size :: Queue a -> Int
size ( Queue [] ) = 0
size ( Queue ( _:xs )) = 1 + size ( Queue xs )
