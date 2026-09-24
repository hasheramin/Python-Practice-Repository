# A Program to validate a five-digit postal code

import re

postal_code = "38000"

pattern = r"^\d{5}$"

if re.fullmatch(pattern, postal_code):
    print("Valid postal code format.")
else:
    print("Invalid postal code format.")


# Explanation:
# ^ and $ ensure that the entire value is checked.
# \d represents a digit.
# {5} requires exactly five digits.

# Therefore values such as:
# 38000
# 44000
# 54000
# match this pattern.
# The pattern checks only the five-digit format, not whether the postal code actually exists.

# Real-Life Use:
# Postal code validation can be used in address and delivery forms.