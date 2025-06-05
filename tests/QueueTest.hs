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


  describe "\n\npeek" $ do
    it "queue with no entries returns nothing" $ do
      peek ( Queue [] ) `shouldBe` ( Nothing :: Maybe Char )


  describe "\n\nsize" $ do
    it "queue with no entries is size zero" $ do
      size ( Queue [] ) `shouldBe` ( 0 :: Int )

    it "queue with one entry is size one" $ do
      size ( Queue [ 3 ]) `shouldBe` ( 1 :: Int )

    it "queue with n entrie is size n" $ do
      size ( Queue [ 0, 1, 2, 3 ]) `shouldBe` ( 4 :: Int )
