# A Program to import functions through a package __init__.py file

from number_tools import square, cube

number = 4

print("Square:", square(number))
print("Cube:", cube(number))

# Explanation:
# __init__.py can expose selected functions from package modules.
# The operations module contains square() and cube().
# __init__.py imports these functions.
# The main program can then import them directly from number_tools.

# Real-Life Use:
# This technique creates a cleaner public interface for packages and hides unnecessary internal details.