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

    it "works with all types, while being type specific" $ do
      peek ( Stack [ 's', 't', 'a', 'r' ]) `shouldBe` ( 's' :: Char )
      peek ( Stack [ "star" ]) `shouldBe` ( "star" :: String )
      peek ( Stack [ 44.44 ]) `shouldBe` ( 44.44 :: Double )
      peek ( Stack [ 0.11 ]) `shouldBe` ( 0.11 :: Float )

  describe "isEmpty" $ do
    it "where no items present, return true" $ do
      isEmpty ( Stack [] ) `shouldBe` True

    it "where items present, return false" $ do
      isEmpty ( Stack [ "value" ]) `shouldBe` False

  describe "size" $ do
    it "where no items, returns zero" $ do
      size ( Stack [] ) `shouldBe` ( 0 :: Int )

    it "where items present, returns number of items present" $ do
      size (( Stack [ 5, 5, 5, 5 ]) :: Stack Int ) `shouldBe` ( 4 :: Int )
