# A Program to build a calculator using a package

from calculator_package import add, subtract, multiply, divide, square, cube

first_number = 10
second_number = 5

print("\nAddition:", add(first_number, second_number))
print("Subtraction:", subtract(first_number, second_number))
print("Multiplication:", multiply(first_number, second_number))
print("Division:", divide(first_number, second_number))
print("Square:", square(first_number))
print("Cube:", cube(second_number))

# Explanation:
# The calculator package separates basic and advanced operations.
# __init__.py exposes the required functions.
# The main program imports those functions directly from the package.
# This creates a clean and reusable calculator structure.

# Real-Life Use:
# Package-based calculators demonstrate how large applications can separate different categories of functionality.