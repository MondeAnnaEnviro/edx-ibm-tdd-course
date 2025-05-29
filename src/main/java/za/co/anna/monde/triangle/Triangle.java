package za.co.anna.monde.triangle;

class Triangle {

    public static double area( double base, double height )
            throws IllegalArgumentException{
        if ( base < 0 && height < 0 )
            throw new IllegalArgumentException(
                    "base and height cannot be negative"
            );

        if ( base < 0 )
            throw new IllegalArgumentException(
                    "base cannot be negative"
            );

        if ( height < 0 )
            throw new IllegalArgumentException(
                    "height cannot be negative"
            );

        return height * base / 2;
    }
}
