module Queue where


newtype Queue a = Queue [ a ] deriving ( Show, Eq )


isEmpty :: Queue a -> Bool
isEmpty ( Queue [] ) = True
