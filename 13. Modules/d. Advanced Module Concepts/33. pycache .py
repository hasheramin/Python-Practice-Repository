# A Program to understand Python's __pycache__ directory

import math

number = 25

print("Square root:", math.sqrt(number))
print("\nPython may create a __pycache__ directory when modules are imported.")

# Explanation:
# When Python imports a module, it can create compiled bytecode files with a .pyc extension.
# These files are normally stored inside a __pycache__ directory.
# Python uses bytecode to help load modules efficiently.
# The __pycache__ directory is generated automatically by Python.

# Real-Life Use:
# Understanding __pycache__ helps developers recognize automatically generated Python files in project directories.