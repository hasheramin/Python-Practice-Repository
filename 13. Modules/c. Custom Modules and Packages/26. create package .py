# A Program to use modules from a custom package

from math_tools import addition, subtraction

print("Addition:", addition.add(20, 10))
print("Subtraction:", subtraction.subtract(20, 10))

# Explanation:
# math_tools is a Python package containing multiple modules.
# __init__.py marks and initializes the package.
# The main program imports modules from the package.
# Each module handles a specific mathematical operation.

# Real-Life Use:
# Packages allow large applications to organize many related modules into meaningful directories.