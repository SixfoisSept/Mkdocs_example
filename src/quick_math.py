class MathOperations:
    """Basic mathematical operations.

    This class provides simple mathematical operations including addition, subtraction,
    multiplication, and division.

    Methods:

    - `add(a, b)`: Add two numbers.

    - `subtract(a, b)`: Subtract two numbers.

    - `multiply(a, b)`: Multiply two numbers.

    - `divide(a, b)`: Divide two numbers. Raises a ValueError if attempting to divide
      by zero.

    Example:
    ```python
    math_ops = MathOperations()
    result_add = math_ops.add(3, 4)  # Returns 7
    result_subtract = math_ops.subtract(5, 2)  # Returns 3
    result_multiply = math_ops.multiply(2, 6)  # Returns 12
    result_divide = math_ops.divide(8, 2)  # Returns 4.0
    ```
    """

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers.

        Args:
            a (float or int): The numerator.
            b (float or int): The denominator.

        Returns:
            float or int: The result of the division.

        Raises:
            ValueError: If attempting to divide by zero.
        """
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")
