module Main where

import Stack
import Test.Hspec

main :: IO ()
main = hspec $ do
    describe "place holder" $ do
        it "place holder" $ do
            sum_ 4 `shouldBe` ( 12 :: Int )
