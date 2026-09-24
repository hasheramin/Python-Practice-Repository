# A Program to validate a date format

import re

date = "21-09-2026"

pattern = r"^\d{2}-\d{2}-\d{4}$"

if re.fullmatch(pattern, date):
    print("Valid date format.")
else:
    print("Invalid date format.")


# Explanation:
# \d{2} matches exactly two digits.
# - matches the hyphen separator.
# \d{4} matches exactly four digits.

# The expected format is:
# DD-MM-YYYY
# This pattern checks the format only.
# For example, it does not determine whether 99-99-2026 is an actual calendar date.

# Real-Life Use:
# Date format validation is useful in forms, records, reports, and data-entry systems.