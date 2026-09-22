# A Program to import multiple functions from a module

from math import sqrt, factorial

number = 5

print("Square root:", sqrt(number))
print("Factorial:", factorial(number))

# Explanation:
# Two functions, sqrt() and factorial(), are imported directly from the math module.
# Both functions can then be used without the math prefix.

# Real-Life Use:
# This approach is useful when a program repeatedly uses a small number of functions from a larger module.