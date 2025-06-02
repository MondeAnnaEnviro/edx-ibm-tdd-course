module Stack where


data Stack a = Stack [ a ] deriving Show


isEmpty :: Stack a -> Bool
isEmpty ( Stack x ) = null x


peek :: Stack a -> a
peek ( Stack x ) = head x
