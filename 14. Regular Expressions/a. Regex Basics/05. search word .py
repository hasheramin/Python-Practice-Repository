# A Program to search for a specific word using a regex pattern

import re

text = "Python makes programming easier."
pattern = r"\bprogramming\b"

result = re.search(pattern, text)

if result:
    print("Word found:", result.group())
else:
    print("Word not found.")

# Explanation:
# \b represents a word boundary in a regular expression.
# It ensures that programming is treated as a complete word.
# re.search() looks for this pattern anywhere in the text.
# The r before the string creates a raw string.

# Real-Life Use:
# Word boundaries are useful when searching for complete words without matching parts of other words.