module Triangle where


area :: Double -> Double -> Either String Double
area base height
 | base < 0 && height < 0  = Left "base and height cannot be negative"
 | base < 0  = Left "base cannot be negative"
 | height < 0  = Left "height cannot be negative"
 | otherwise = Right $ height * base / 2
