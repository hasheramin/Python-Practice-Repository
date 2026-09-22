# A Program to build a calculator using a custom module to perform basic arithmetic operations

import calculator_operations

first_number = 25
second_number = 5

print("Addition:", calculator_operations.add(first_number, second_number))
print("Subtraction:", calculator_operations.subtract(first_number, second_number))
print("Multiplication:", calculator_operations.multiply(first_number, second_number))
print("Division:", calculator_operations.divide(first_number, second_number))

# Explanation:
# The calculator logic is placed inside a separate module.
# The main program only provides the input and uses the functions.
# This separates calculation logic from program interaction.
# The module can now be reused by other programs.

# Real-Life Use:
# Separating business logic into modules makes applications easier to test, reuse, and expand.