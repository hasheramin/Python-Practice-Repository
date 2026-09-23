# A Program to find non-digit characters

import re

text = "Python 123"

pattern = r"\D"

matches = re.findall(pattern, text)

print("Non-digit characters:", matches)


# Explanation:
# \D represents any character that is NOT a digit.
# re.findall() returns every non-digit character.
# Spaces and letters are also considered non-digit characters, so they are included in the result.
# \D is useful when we want to detect everything except numeric characters.

# Real-Life Use:
# Non-digit matching can help identify separators, text, spaces, or unwanted characters in numeric input.