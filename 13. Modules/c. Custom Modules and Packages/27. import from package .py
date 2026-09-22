# A Program to import specific functions from a package

from user_tools.validator import validate_username
from user_tools.formatter import format_username

username = "  Hasher  "

formatted_username = format_username(username)
is_valid = validate_username(formatted_username)

print("Username:", formatted_username)
print("Valid:", is_valid)

# Explanation:
# Specific functions can be imported directly from package modules.
# formatter.py provides the formatting function.
# validator.py provides the validation function.
# The main program combines both functions.

# Real-Life Use:
# Direct imports are useful when a project contains many modules but only a few functions are required.