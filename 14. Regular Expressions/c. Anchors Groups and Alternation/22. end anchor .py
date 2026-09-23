# A Program to match a pattern at the end of a string

import re

text = "I am learning Python"

pattern = r"Python$"

match = re.search(pattern, text)

if match:
    print("Pattern found at the end.")
else:
    print("Pattern not found at the end.")


# Explanation:
# $ is the end anchor.
# It tells the regular expression that the pattern must appear at the end of the string.
# Python$ means that "Python" must be at the end.
# Since our text ends with Python, the pattern matches.

# Real-Life Use:
# The end anchor can be useful for checking file extensions, suffixes, and formatted input.