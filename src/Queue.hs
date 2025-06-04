module Queue where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


empty :: Queue a
empty = Queue []


size :: Queue a -> Int
size ( Queue [] ) = 0
