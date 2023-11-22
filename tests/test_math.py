import unittest
from src.my_package import quick_math

class TestMathOperations(unittest.TestCase):

    def test_add_numbers(self):
        result = quick_math.add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_subtract_numbers(self):
        result = quick_math.subtract_numbers(5, 3)
        self.assertEqual(result, 2)

    def test_multiply_numbers(self):
        result = quick_math.multiply_numbers(2, 3)
        self.assertEqual(result, 6)

    def test_divide_numbers(self):
        result = quick_math.divide_numbers(6, 2)
        self.assertEqual(result, 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            quick_math.divide_numbers(5, 0)

if __name__ == '__main__':
    unittest.main()
