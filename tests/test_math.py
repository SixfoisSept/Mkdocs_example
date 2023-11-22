import unittest
from src.quick_math import MathOperations

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        math_operations = MathOperations()
        result = math_operations.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        math_operations = MathOperations()
        result = math_operations.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiplication(self):
        math_operations = MathOperations()
        result = math_operations.multiply(4, 6)
        self.assertEqual(result, 24)

    def test_division(self):
        math_operations = MathOperations()
        result = math_operations.divide(8, 2)
        self.assertEqual(result, 4)

    def test_division_by_zero(self):
        math_operations = MathOperations()
        with self.assertRaises(ValueError) as context:
            math_operations.divide(10, 0)

        self.assertEqual(
            str(context.exception),
            "Cannot divide by zero."
        )
