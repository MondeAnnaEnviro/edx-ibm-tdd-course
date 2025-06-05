module Main where


import Test.Hspec
import Queue


main :: IO ()
main = hspec $ do


  describe "\n\nisEmpty" $ do
    it "queue with no entries returns true" $ do
      isEmpty ( Queue [] ) `shouldBe` True
