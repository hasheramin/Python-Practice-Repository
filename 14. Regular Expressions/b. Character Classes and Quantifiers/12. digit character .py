# A Program to find all digit characters

import re

text = "My marks are 85 and my roll number is 27."

pattern = r"\d"

matches = re.findall(pattern, text)

print("Digits:", matches)


# Explanation:
# \d represents a digit character.
# re.findall() checks the entire text and collects every digit that matches \d.
# Notice that each digit is returned separately.
# For example, 85 becomes "8" and "5".
# Later, quantifiers can be combined with \d to match complete numbers.

# Real-Life Use:
# \d can be used to detect numbers such as ages, IDs, marks, dates, and other numeric input.