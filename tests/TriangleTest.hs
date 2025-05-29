module Main where


import Triangle
import Test.Hspec


main :: IO ()
main = hspec $ do
  describe "area of a triangle" $ do
    context "input types" $ do
      it "when values are doubles" $ do
        area 3.4556 8.3567  `shouldBe` Right 14.43870626
        area 2.3    5.7     `shouldBe` Right  6.555

      it "when values are integers" $ do
        area 2 5 `shouldBe` Right  5.0
        area 4 6 `shouldBe` Right 12.0

    context "zero as input" $ do
      it "when base is zero" $ do
        area 0 5 `shouldBe` Right 0.0

      it "when height is zero" $ do
        area 2 0 `shouldBe` Right 0.0

      it "when base and height are zero" $ do
        area 0 0 `shouldBe` Right 0.0

    context "inform user of invalid input values" $ do
      it "when base is negative" $ do
        let message = "base cannot be negative"
        area (- 2) 5 `shouldBe` Left message

      it "when height is negative" $ do
        let message = "height cannot be negative"
        area 2 (-5) `shouldBe` Left message

      it "when both base and height are negative" $ do
        let message = "base and height cannot be negative"
        area (-2) (-5) `shouldBe` Left message
