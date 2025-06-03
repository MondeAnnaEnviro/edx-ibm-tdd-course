module Main where


import Stack
import Test.Hspec


main :: IO ()
main = hspec $ do


  describe "\n\nisEmpty" $ do
    it "where no items present, return true" $ do
      isEmpty empty `shouldBe` True

    it "where items present, return false" $ do
      let stack = Stack [ "value" ]
      isEmpty stack `shouldBe` False


  describe "\n\npeek" $ do
    it "where no item present, shows nothing" $ do
      peek empty `shouldBe` ( Nothing :: Maybe String )
      peek empty `shouldBe` ( Nothing :: Maybe Char )
      peek empty `shouldBe` ( Nothing :: Maybe Int )

    it "where one item present, said item shows" $ do
      let stack = Stack [ 44 ]
      peek stack `shouldBe` ( Just 44 :: Maybe Int )

    it "where many items present, left-most item shows" $ do
      {- recall: adding uses `cons`, thus prepends to list
       - consequently, the left most item is the last addition
       -}
      let stack = Stack [ 653, 1, 66, 903, 43 ]
      peek stack `shouldBe` ( Just 653 :: Maybe Int )

    it "works with all types, while being type specific" $ do
      let chars = Stack [ 'c', 'h', 'a', 'r', 's' ]
      peek chars `shouldBe` ( Just 'c' :: Maybe Char )

      let strs = Stack [ "star" ]
      peek strs `shouldBe` ( Just "star" :: Maybe String )

      let doubles = Stack [ 44.44 ]
      peek doubles `shouldBe` ( Just 44.44 :: Maybe Double )

      let floats = Stack [ 0.11 ]
      peek floats `shouldBe` ( Just 0.11 :: Maybe Float )


  describe "\n\npop" $ do
    it "where no items present, returns nothing" $ do
      pop ( empty :: Stack String ) `shouldBe` ( Nothing, empty :: Stack a )
      pop ( empty :: Stack Char ) `shouldBe` ( Nothing, empty :: Stack a )
      pop ( empty :: Stack Int ) `shouldBe` ( Nothing, empty :: Stack a )

    it "where one item present, returns item and smaller stack" $ do
      let stack = Stack [ "single" ]
      let ( item, smallerStack ) = pop stack

      item `shouldBe` ( Just "single" :: Maybe String )
      size stack `shouldBe` ( 1 :: Int )
      size smallerStack `shouldBe` ( 0 :: Int )

    it "where many items present, returns left-most item" $ do
      let stack = Stack [ "left", "middle", "right" ]
      let ( item, smallerStack ) = pop stack

      item `shouldBe` ( Just "left" :: Maybe String )
      size stack `shouldBe` ( 3 :: Int )
      size smallerStack `shouldBe` ( 2 :: Int )


  describe "\n\npush" $ do
    it "where no items present, should add one item" $ do
      let stack = push "word" empty

      isEmpty stack `shouldBe` False
      peek stack `shouldBe` ( Just "word" :: Maybe String )
      size stack `shouldBe` ( 1 :: Int )

    it "n pushes makes for n sized stack" $ do
      let stack = push 4 $ push 77 $ push 4 empty
      size ( stack :: Stack Int ) `shouldBe` ( 3 :: Int )
      size stack `shouldBe` ( 3 :: Int )

    it "ensure 'last in; first out' pattern" $ do
      let first = push "first" empty
      let second = push "second" first
      let third = push "third" second

      size first `shouldBe` ( 1 :: Int )
      size second `shouldBe` ( 2 :: Int )
      size third `shouldBe` ( 3 :: Int )

      peek first `shouldBe` ( Just "first" :: Maybe String )
      peek second `shouldBe` ( Just "second" :: Maybe String )
      peek third `shouldBe` ( Just "third" :: Maybe String )


  describe "\n\nsize" $ do
    it "where no items, returns zero" $ do
      size empty `shouldBe` ( 0 :: Int )

    it "where items present, returns number of items present" $ do
      let stack = Stack [ 5, 5, 5, 5 ] :: Stack Int
      size stack `shouldBe` ( 4 :: Int )
