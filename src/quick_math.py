"""
quick_math.py

This module contains functions for basic mathematical operations.

Functions:
- add_numbers: Adds two numbers.
- subtract_numbers: Subtracts the second number from the first.
- multiply_numbers: Multiplies two numbers.
- divide_numbers: Divides the first number by the second.

Usage:
    import quick_math

    result = quick_math.add_numbers(2, 3)
    print(result)  # Output: 5
"""

def add_numbers(a, b):
    """
    Adds two numbers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtracts the second number from the first.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    int or float: The result of subtracting the second number from the first.
    """
    return a - b

def multiply_numbers(a, b):
    """
    Multiplies two numbers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    int or float: The product of the two numbers.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divides the first number by the second.

    Parameters:
    - a (int or float): The numerator.
    - b (int or float): The denominator (must not be zero).

    Returns:
    float: The result of dividing the first number by the second.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
