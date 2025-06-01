module Stack where


data Stack a = Stack [ a ] deriving Show


peek :: Stack a -> a
peek ( Stack x ) = head x
