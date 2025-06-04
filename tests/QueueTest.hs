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

    it "a queue with n elements is a size of n" $ do
      size ( Queue [ 0, 1, 2 ]) `shouldBe` ( 3 :: Int )


  describe "\n\nisEmpty" $ do
    it "a queue with no elements is empty" $ do
      isEmpty empty `shouldBe` True

    it "a queue with elements is not empty" $ do
      isEmpty ( Queue [ 3 ]) `shouldBe` False

  describe "\n\npeek" $ do
    it "an empty queue shows nothing" $ do
      peek empty `shouldBe` ( Nothing :: Maybe Char )

    it "a queue with one element shows said elelment" $ do
      peek ( Queue [ "1" ])  `shouldBe` ( Just "1" :: Maybe String )

    it "a queue with multiple elements shows right most element" $ do
      peek ( Queue [ 0, 1, 2, 3, 4, 5 ]) `shouldBe` ( Just 5 :: Maybe Int )


  describe "\n\npush" $ do
    it "an empty queue produces a queue of one entry after push" $ do
      let queue = push "init" empty

      isEmpty queue `shouldBe` False
      size queue `shouldBe` ( 1 :: Int )
      peek queue `shouldBe` ( Just "init" :: Maybe String )
