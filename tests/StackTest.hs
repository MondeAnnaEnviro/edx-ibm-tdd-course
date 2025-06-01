module Main where

import Stack
import Test.Hspec

main :: IO ()
main = hspec $ do

  describe "peek" $ do
    it "where one item present, said item shows" $ do
      peek ( Stack [ 44 ]) `shouldBe` ( 44 :: Int )
