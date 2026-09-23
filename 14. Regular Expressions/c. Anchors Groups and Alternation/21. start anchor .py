# A Program to match a pattern at the start of a string

import re

text = "Python is easy to learn."

pattern = r"^Python"

match = re.search(pattern, text)

if match:
    print("Pattern found at the beginning.")
else:
    print("Pattern not found at the beginning.")


# Explanation:
# ^ is the start anchor.
# It tells the regular expression that the pattern must begin at the start of the string.
# ^Python means that "Python" must appear at the beginning of the text.
# Since our text starts with Python, the pattern matches.

# Real-Life Use:
# The start anchor can be used when validating prefixes, commands, usernames, or formatted input.