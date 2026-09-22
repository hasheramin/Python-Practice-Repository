# A Program to use a utility module

import utilities

number = 24

print("Is even:", utilities.is_even(number))

percentage = utilities.calculate_percentage(45, 60)
print("Percentage:", percentage)

name = utilities.format_name("hasher", "amin")
print("Formatted name:", name)

# Explanation:
# utilities.py contains small reusable helper functions.
# The main program imports the module and calls the required functions.
# Keeping helper logic in one module prevents repeated code.
# The same utilities can be reused in multiple programs.

# Real-Life Use:
# Utility modules are common in real projects for validation, formatting, calculations, conversions, and shared helper logic.