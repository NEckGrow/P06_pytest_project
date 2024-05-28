from calculator.calculator import Calculator
import pytest
class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        #arrange
        a=5555
        b=4321
        cal=Calculator()

        #act 
        result=cal.subtract(a,b)

        #assert
        expected= 1234
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 5
        b = 6
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 30
        
        assert result == expected

    def test_divide(self):
        # arrange
        a = 5555
        b = 5
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 1111
        assert result == expected

    def test_zero_error(self):
         # arrange
        a = 5555
        b = 0
        cal = Calculator()

        # act
        

        # assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a, b)
    



    

   


