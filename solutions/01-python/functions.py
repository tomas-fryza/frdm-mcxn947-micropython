"""
Digital Electronics Lab
Board: FRDM-MCXN947
Example: Usage of MicroPython functions

Author: Tomas Fryza
Created: 2023-10-12
Last modified: 2026-01-27
"""

import time
import math
import cmath  # Complex numbers' math


def counters():
    # Example 1: Percentage counter
    values = range(0, 100)
    for i in values:
        print(f"{i} %", end="\r")
        time.sleep_ms(50)
    print("\nProcess complete!")

    # Example 2: Spinner animation
    symbols = ["/", "-", "\\", "|"]
    for i in range(10):
        for symbol in symbols:
            print(f"Processing... {symbol}", end="\r")
            time.sleep_ms(50)
    print("Processing... Done")


# Returns the factorial of a given non-negative integer n
def factorial(n):
    """Compute n! for n >= 0."""
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return

    result = 1
    while n > 1:
        result = result * n
        n = n - 1

    return result


def triangle(lines):
    """Prints the triangle of asterics `*`."""
    for i in range(lines):
        print("#" * (i+1))


def fibonacci(n):
    a, b = 0, 1
    start_time = time.ticks_us()  # Start time in microseconds

    for _ in range(n):
        a, b = b, a+b

    end_time = time.ticks_us()
    duration = end_time - start_time

    print(f"Length of Fibonacci sequence: {n}")
    print(f"Last calculated value: {b}")
    print(f"Time elapsed: {duration} us")


def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discr = b**2 - 4*a*c

    # Check the discriminant for real solutions
    if discr == 0:
        x1 = -b / (2*a)
        x2 = x1  # One real root (repeated)
    elif discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2*a)
        x2 = (-b - math.sqrt(discr)) / (2*a)
        # Two distinct real roots
    else:
        # Complex roots (no real solutions)
        x1 = (-b+cmath.sqrt(discr)) / (2*a)
        x2 = (-b-cmath.sqrt(discr)) / (2*a)

    return x1, x2


if __name__ == "__main__":
    # counters()

    # n = 7
    # print(f"The factorial of {n} is {factorial(n)}")

    # triangle(5)
    fibonacci(20)

    # a, b, c = 1, 5, 1
    # roots = solve_quadratic(a, b, c)
    # print(f"Roots of {a}x^2 + {b}x + {c} = 0: {roots}")


    # NOTE: In Thonny IDE, enable `\r` and ANSI-color
    #       support in menu:
    #   Tools > Options... > Shell > Terminal emulation (...)
    # print("This is \x1b[1;32mGreen and Bold\x1b[0m")
    # print("\x1b[1;31m[ERROR]\x1b[0m End of file")
