# A Program to find a Pakistani phone number inside text

import re

text = "Contact Ali at 03161242567 for details."
pattern = r"\b03\d{9}\b"

result = re.search(pattern, text)

if result:
    print("Phone number found:", result.group())
else:
    print("Phone number not found.")

# Explanation:
# \b ensures that we match a complete number.
# 03 matches the common starting prefix.
# \d matches a digit.
# {9} requires exactly nine additional digits.
# Together, the pattern matches an 11-digit number beginning with 03.

# Real-Life Use:
# Regex phone patterns can be used for basic form validation and extracting phone numbers from text.