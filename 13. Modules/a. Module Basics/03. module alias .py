# A Program to use an alias for a module

import math as m

number = 81

print("Square root:", m.sqrt(number))
print("Value of pi:", m.pi)

# Explanation:
# The math module is imported with the alias m.
# The alias provides a shorter name for the module.
# We then access sqrt() and pi using m.

# Real-Life Use:
# Aliases are useful when module names are long or when a commonly used short name is preferred.