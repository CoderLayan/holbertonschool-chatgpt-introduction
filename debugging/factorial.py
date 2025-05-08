#!/usr/bin/python3
import sys

def factorial(n):
    result = 1  # This line must be **indented**
    while n > 1:  # Ensure this block is also properly indented
        result *= n
        n -= 1  

    return result  # Indentation must be consistent

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
