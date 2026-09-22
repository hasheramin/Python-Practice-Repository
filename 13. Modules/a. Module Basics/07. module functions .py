# A Program to use functions from a custom module for basic arithmetic operations

import calculator

first_number = 20
second_number = 5

print("Addition:", calculator.add(first_number, second_number))
print("Subtraction:", calculator.subtract(first_number, second_number))
print("Multiplication:", calculator.multiply(first_number, second_number))
print("Division:", calculator.divide(first_number, second_number))

# Explanation:
# calculator.py contains reusable mathematical functions.
# The main program imports the calculator module.
# Each function is called using calculator.function_name().
# This separates calculations from the main program logic.

# Real-Life Use:
# Large applications often keep related functionality inside separate utility modules for better organization.