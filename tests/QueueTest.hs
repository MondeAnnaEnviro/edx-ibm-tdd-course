module Main where


import Test.Hspec
import Queue


main :: IO ()
main = hspec $ do


  describe "\n\nsize" $ do
    it "the size of an empty queue is zero" $ do
      size empty `shouldBe` ( 0 :: Int )

    it "the size of a queue with one element is one" $ do
      size ( Queue [ 1 ]) `shouldBe` ( 1 :: Int )
