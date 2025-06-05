module Main where


import Test.Hspec
import Queue


main :: IO ()
main = hspec $ do


  describe "\n\ndequeue" $ do
    it "queue with no entries returns nothing and empty queue" $ do
      let ( nothing, dequeued ) = dequeue empty
      nothing `shouldBe` ( Nothing :: Maybe Double )
      isEmpty dequeued `shouldBe` True

    it "queue with one entries returns said entry and empty queue" $ do
      let ( entry, dequeued ) = dequeue $ enqueue 1 empty
      entry `shouldBe` ( Just 1 :: Maybe Double )
      isEmpty dequeued `shouldBe` True

    it "queue with n entries returns first entry and size n-1 queue" $ do
      let queue = enqueue 2 $ enqueue 1 $ enqueue 0 empty
      let ( entry, dequeued ) = dequeue queue

      entry `shouldBe` ( Just 0 :: Maybe Int )

      peek dequeued `shouldBe` ( Just 1 :: Maybe Int )
      size dequeued `shouldBe` ( 2 :: Int )


  describe "\n\nenqueue" $ do
    it "properties after one enqueue" $ do
      let queue = enqueue "one" empty

      peek queue `shouldBe` ( Just "one" :: Maybe String )
      size queue `shouldBe` ( 1 :: Int )
      isEmpty queue `shouldBe` False

    it "properties after multiple enqueues" $ do
      let queue = enqueue 'c' $ enqueue 'b' $ enqueue 'a' empty

      peek queue `shouldBe` ( Just 'a' :: Maybe Char )
      size queue `shouldBe` ( 3 :: Int )
      isEmpty queue `shouldBe` False


  describe "\n\nisEmpty" $ do
    it "queue with no entries returns true" $ do
      isEmpty empty `shouldBe` True

    it "queue entries returns false" $ do
      let queue = enqueue 1 empty
      isEmpty queue `shouldBe` False


  describe "\n\npeek" $ do
    it "queue with no entries returns nothing" $ do
      peek empty `shouldBe` ( Nothing :: Maybe Char )

    it "queue with one entry returns entry" $ do
      let queue = enqueue "show" empty
      peek queue `shouldBe` ( Just "show" :: Maybe String )

    it "queue with n entries returns first entry" $ do
      let queue = enqueue 3 $ enqueue 2 $ enqueue 1 empty
      peek queue `shouldBe` ( Just 1 :: Maybe Int )


  describe "\n\nsize" $ do
    it "queue with no entries is size zero" $ do
      size empty `shouldBe` ( 0 :: Int )

    it "queue with one entry is size one" $ do
      let queue = enqueue 3 empty
      size queue `shouldBe` ( 1 :: Int )

    it "queue with n entrie is size n" $ do
      let queue = enqueue 2 $ enqueue 1 $ enqueue 0 empty
      size queue `shouldBe` ( 3 :: Int )
