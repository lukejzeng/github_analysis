```python
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

# Get input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum_result = calculate_sum(num1, num2)
    print("The sum of", num1, "and", num2, "is:", sum_result)
except ValueError:
    print("Invalid input. Please enter numbers only.")

```