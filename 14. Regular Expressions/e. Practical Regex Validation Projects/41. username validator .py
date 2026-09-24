# A Program to validate a username using regular expressions

import re

username = "hasher_amin"

pattern = r"^[A-Za-z0-9_]{3,20}$"

if re.fullmatch(pattern, username):
    print("Valid username.")
else:
    print("Invalid username.")


# Explanation:
# ^ and $ ensure that the complete string is checked.
# [A-Za-z0-9_] allows:
# - uppercase letters
# - lowercase letters
# - digits
# - underscore

# {3,20} means the username must contain between 3 and 20 characters.
# re.fullmatch() checks that the entire string matches the pattern.

# Real-Life Use:
# Username validation is commonly used during account registration and profile creation.