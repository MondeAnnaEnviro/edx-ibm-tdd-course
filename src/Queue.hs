module Queue where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


isEmpty :: Queue a -> Bool
isEmpty ( Queue [] ) = True
isEmpty ( Queue _ ) = False


size :: Queue a -> Int
size ( Queue [] ) = 0
size ( Queue x ) = 1
