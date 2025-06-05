module Queue where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


isEmpty :: Queue a -> Bool
isEmpty ( Queue [] ) = True
isEmpty ( Queue _ ) = False


peek :: Queue a -> Maybe a
peek ( Queue [] ) = Nothing


size :: Queue a -> Int
size ( Queue [] ) = 0
size ( Queue ( x:xs ))
 | isEmpty ( Queue xs ) = 1
 | otherwise = 1 + size ( Queue xs )
