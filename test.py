```python
import unittest

def calculate_sum(num1, num2):
    """Calculates the sum of two numbers.

    Args:
      num1: The first number.
      num2: The second number.

    Returns:
      The sum of num1 and num2.  Returns an error message if input is not a number.

    """
    if not isinstance(num1,(int,float)) or not isinstance(num2,(int,float)):
        return "Error: Inputs must be numbers."
    return num1 + num2

class TestCalculateSum(unittest.TestCase):
    def test_valid_integer_inputs(self):
        self.assertEqual(calculate_sum(5, 3), 8)

    def test_valid_float_inputs(self):
        self.assertEqual(calculate_sum(5.5, 3.5), 9.0)

    def test_mixed_integer_float_inputs(self):
        self.assertEqual(calculate_sum(5, 3.5), 8.5)

    def test_invalid_string_input(self):
        self.assertEqual(calculate_sum("5", 3), "Error: Inputs must be numbers.")

    def test_invalid_mixed_input(self):
        self.assertEqual(calculate_sum(5, "abc"), "Error: Inputs must be numbers.")

    def test_invalid_both_inputs(self):
        self.assertEqual(calculate_sum("abc","def"), "Error: Inputs must be numbers.")

    def test_zero_input(self):
        self.assertEqual(calculate_sum(0,0),0)

    def test_negative_input(self):
        self.assertEqual(calculate_sum(-5,-3),-8)

    def test_large_numbers(self):
        self.assertEqual(calculate_sum(1000000,2000000),3000000)


if __name__ == '__main__':
    unittest.main()
```