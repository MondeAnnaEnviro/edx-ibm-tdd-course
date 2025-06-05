module Queue where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


empty :: Queue a
empty = Queue []


isEmpty :: Queue a -> Bool
isEmpty ( Queue [] ) = True
isEmpty ( Queue _ ) = False


peek :: Queue a -> Maybe a
peek ( Queue [] ) = Nothing
peek ( Queue ( x:xs ))
 | isEmpty ( Queue xs ) = Just x
 | otherwise = peek ( Queue xs )


dequeue :: Queue a -> ( Maybe a, Queue a )
dequeue ( Queue [] ) = ( Nothing, Queue [] )
dequeue ( Queue ( x:xs ))
 | isEmpty ( Queue xs ) = ( Just x, Queue [] )
 | otherwise = ( peek ( Queue xs ), Queue ( x : init xs ))


enqueue :: a -> Queue a -> Queue a
enqueue x ( Queue [] ) = Queue [ x ]
enqueue x ( Queue xs ) = Queue ( x:xs )


size :: Queue a -> Int
size ( Queue [] ) = 0
size ( Queue ( x:xs ))
 | isEmpty ( Queue xs ) = 1
 | otherwise = 1 + size ( Queue xs )
