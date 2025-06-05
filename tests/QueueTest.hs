module Main where


import Test.Hspec
import Queue


main :: IO ()
main = hspec $ do


  describe "\n\nisEmpty" $ do
    it "queue with no entries returns true" $ do
      isEmpty ( Queue [] ) `shouldBe` True

    it "queue entries returns false" $ do
      isEmpty ( Queue [ 1 ] ) `shouldBe` False


  describe "\n\nsize" $ do
    it "queue with no entries is size zero" $ do
      size ( Queue [] ) `shouldBe` ( 0 :: Int )
