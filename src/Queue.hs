module Queue where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


empty :: Queue a
empty = Queue []


isEmpty :: Queue a -> Bool
isEmpty ( Queue x ) = size ( Queue x ) == 0


peek :: Queue a -> Maybe a
peek ( Queue [] ) = Nothing
peek ( Queue [ x ]) = Just x


size :: Queue a -> Int
size ( Queue [] ) = 0
size ( Queue ( _:xs )) = 1 + size ( Queue xs )
