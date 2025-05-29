package za.co.anna.monde.triangle;

import static org.assertj.core.api.Assertions.assertThatIllegalArgumentException;
import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class TriangleTest {

    @Test
    public void whenValuesAreDoubles(){
        assertThat( Triangle.area( 3.4556, 8.3567 )).isEqualTo( 14.43870626 );
        assertThat( Triangle.area( 2.3, 5.7 )).isEqualTo( 6.555 );
    }

    @Test
    public void whenValuesAreIntegers(){
        assertThat( Triangle.area( 2, 5 )).isEqualTo(  5.0 );
        assertThat( Triangle.area( 4, 6 )).isEqualTo( 12.0 );
    }

    @Test
    public void whenBaseIsZero(){
        assertThat( Triangle.area( 0, 5 )).isEqualTo(  0.0 );
    }

    @Test
    public void whenHeightIsZero(){
        assertThat( Triangle.area( 2, 0 )).isEqualTo(  0.0 );
    }

    @Test
    public void whenBaseAndHeightAreZero(){
        assertThat( Triangle.area( 0, 0 )).isEqualTo(  0.0 );
    }

    @Test
    public void whenBaseAndHeightAreNegative(){
        assertThatIllegalArgumentException()
                .isThrownBy(() ->Triangle.area( -2, -5 ))
                .withMessage( "base and height cannot be negative" );
    }

    @Test
    public void whenBaseIsNegative(){
        assertThatIllegalArgumentException()
                .isThrownBy(() ->Triangle.area( -2, 5 ))
                .withMessage( "base cannot be negative" );
    }

    @Test
    public void whenHeightIsNegative(){
        assertThatIllegalArgumentException()
                .isThrownBy(() ->Triangle.area( 2, -5 ))
                .withMessage( "height cannot be negative" );
    }
}
