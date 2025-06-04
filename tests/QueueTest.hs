module Main where


import Test.Hspec
import Queue


main :: IO ()
main = hspec $ do


  describe "\n\nisEmpty" $ do
    it "a queue with no elements is empty" $ do
      isEmpty empty `shouldBe` True

    it "a queue with elements is not empty" $ do
      let queue = ( push 3 empty ) :: Queue Int
      isEmpty queue `shouldBe` False

  describe "\n\npeek" $ do
    it "an empty queue shows nothing" $ do
      peek empty `shouldBe` ( Nothing :: Maybe Char )

    it "a queue with one element shows said elelment" $ do
      let queue = push "1" empty
      peek queue  `shouldBe` ( Just "1" :: Maybe String )

    it "a queue with multiple elements shows first addition" $ do
      let queue = push 0 $ push 1 $ push 2 $ push 3 empty
      peek queue `shouldBe` ( Just 3 :: Maybe Int )


  describe "\n\npush" $ do
    it "an empty queue produces a queue of one entry after push" $ do
      let queue = push "init" empty

      isEmpty queue `shouldBe` False
      size queue `shouldBe` ( 1 :: Int )
      peek queue `shouldBe` ( Just "init" :: Maybe String )

    it "n pushes renders queue with n properties" $ do
      let queue = push "last" $ push "second" $ push "first" empty

      isEmpty queue `shouldBe` False
      size queue `shouldBe` ( 3 :: Int )
      peek queue `shouldBe` ( Just "first" :: Maybe String )


  describe "\n\nsize" $ do
    it "the size of an empty queue is zero" $ do
      size empty `shouldBe` ( 0 :: Int )

    it "the size of a queue with one element is one" $ do
      let queue = ( push 1 empty ) :: Queue Int
      size queue `shouldBe` ( 1 :: Int )

    it "a queue with n elements is a size of n" $ do
      let queue = push 0 $ push 1 $ push 2 empty
      size ( queue :: Queue Int ) `shouldBe` ( 3 :: Int )
