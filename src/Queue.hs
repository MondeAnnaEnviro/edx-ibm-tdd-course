module Queue ( Queue, empty, isEmpty, peek, pop, push, size ) where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


empty :: Queue a
empty = Queue []


isEmpty :: Queue a -> Bool
isEmpty ( Queue x ) = size ( Queue x ) == 0


{-
 - NOTE: using builtins, the recursive
 - call could have been replaced with
 - `otherwise = head $ reverse xs`
-}
peek :: Queue a -> Maybe a
peek ( Queue [] ) = Nothing
peek ( Queue ( x:xs ))
 | size ( Queue xs ) == 0 = Just x
 | otherwise = peek ( Queue xs )


pop :: Queue a -> ( Maybe a, Queue a )
pop ( Queue [] ) = ( Nothing, Queue [] )
pop ( Queue [ x ]) = ( Just x, Queue [] )
pop ( Queue ( x:xs )) = ( Just $ head $ reverse xs, Queue $ init $ x:xs )
 -- unable to come up with a solution that does not use builtins


push :: a -> Queue a -> Queue a
push x ( Queue [] ) = Queue [ x ]
push x ( Queue xs ) = Queue ( x:xs)


size :: Queue a -> Int
size ( Queue [] ) = 0
size ( Queue ( _:xs )) = 1 + size ( Queue xs )
