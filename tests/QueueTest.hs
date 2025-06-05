module Main where


import Test.Hspec
import Queue


main :: IO ()
main = hspec $ do


  describe "\n\nlinkage" $ do
    it "linked to queues src script" $ do
      linkage `shouldBe` True
