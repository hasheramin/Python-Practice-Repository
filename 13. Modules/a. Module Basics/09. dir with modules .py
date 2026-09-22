# A Program to inspect the contents of a module using dir()

import math

items = dir(math)

print("Number of available items:", len(items))

print("\nFirst 10 items:")
for item in items[:10]:
    print(item)

# Explanation:
# dir() returns a list of names available inside an object or module.
# Here it is used with the math module.
# The list is stored in items and then we display some entries.
# This helps us explore what functionality a module provides.

# Real-Life Use:
# dir() is useful during development when exploring unfamiliar modules and understanding which functions, classes, and variables are available.