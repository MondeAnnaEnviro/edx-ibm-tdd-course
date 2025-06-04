module Queue where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


empty :: Queue a
empty = Queue []


size :: Queue a -> Int
size ( Queue [] ) = 0
size ( Queue [ _ ]) = 1
size ( Queue ( x:xs )) = 1 + size ( Queue xs )
