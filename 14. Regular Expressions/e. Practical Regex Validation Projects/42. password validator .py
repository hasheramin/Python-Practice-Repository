# A Program to validate a password using regular expressions

import re

password = "Python@123"

has_length = re.search(r".{8,}", password)
has_uppercase = re.search(r"[A-Z]", password)
has_lowercase = re.search(r"[a-z]", password)
has_digit = re.search(r"\d", password)
has_special = re.search(r"[^A-Za-z0-9]", password)

if (
    has_length
    and has_uppercase
    and has_lowercase
    and has_digit
    and has_special
):
    print("Password meets the required format.")
else:
    print("Password does not meet the required format.")


# Explanation:
# The password is checked using several independent patterns.
# .{8,} checks for at least 8 characters.
# [A-Z] checks for an uppercase letter.
# [a-z] checks for a lowercase letter.
# \d checks for a digit.
# [^A-Za-z0-9] checks for a special character.

# All conditions must be satisfied.
# This example demonstrates how multiple regex checks can work together instead of creating one very complex regular expression.

# Real-Life Use:
# Password format validation can be used during account registration and password creation.