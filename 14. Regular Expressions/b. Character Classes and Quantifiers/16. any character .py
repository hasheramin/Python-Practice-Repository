# A Program to match any single character

import re

text = "cat cut cot"

pattern = r"c.t"

matches = re.findall(pattern, text)

print("Matches:", matches)


# Explanation:
# The dot (.) matches any single character except a newline by default.

# The pattern c.t means:
# c -> must be the letter c
# . -> any single character
# t -> must be the letter t
# Therefore, cat, cut, and cot all match the pattern.

# Real-Life Use:
# The dot can be useful when a known pattern contains one unknown character.