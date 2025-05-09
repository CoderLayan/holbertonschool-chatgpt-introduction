#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a given number.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial(n-1)
        return n * factorial(n-1)

# Read the command-line argument, convert it to an integer, and compute the factorial
f = factorial(int(sys.argv[1]))

# Print the result to the console
print(f)
