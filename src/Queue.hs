module Queue where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


empty :: Queue a
empty = Queue []


size :: Queue a -> Int
size ( Queue [] ) = 0
size ( Queue ( _:xs )) = 1 + size ( Queue xs )


isEmpty :: Queue a -> Bool
isEmpty ( Queue [] ) = True
