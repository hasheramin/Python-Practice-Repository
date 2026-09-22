# A Program to match a pattern from the beginning of text

import re

text = "Python is easy to learn."
pattern = "Python"

result = re.match(pattern, text)

if result:
    print("Pattern matched:", result.group())
else:
    print("Pattern did not match.")

# Explanation:
# re.match() checks the pattern only at the beginning of the string.
# Since Python is the first word, the pattern matches successfully.
# Unlike re.search(), match() does not search the entire string.

# Real-Life Use:
# re.match() is useful when input must begin with a specific prefix or pattern.