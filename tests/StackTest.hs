module Main where

import Stack
import Test.Hspec

main :: IO ()
main = hspec $ do

  describe "peek" $ do
    it "where one item present, said item shows" $ do
      peek ( Stack [ 44 ]) `shouldBe` ( 44 :: Int )

    it "where many items present, left-most item shows" $ do
      {- recall: adding uses `cons`, thus prepends to list
       - consequently, the left most item is the last addition
       -}
      peek ( Stack [ 653, 1, 66, 903, 43 ]) `shouldBe` ( 653 :: Int )
