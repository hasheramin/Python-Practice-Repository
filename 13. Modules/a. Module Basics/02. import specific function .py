# A Program to import a specific function from a module

from math import sqrt

number = 64
result = sqrt(number)

print("Square root:", result)

# Explanation:
# Instead of importing the complete math module, we import only the sqrt() function.
# Because sqrt() was imported directly, we can call it without writing math.sqrt().

# Real-Life Use:
# Importing only required functions can make code shorter and clearly show which functionality a program needs.