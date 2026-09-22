# A Program to import and use the re module

import re

text = "Python is a powerful programming language."
pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Pattern found.")
else:
    print("Pattern not found.")

# Explanation:
# The re module provides Python's regular expression functionality.
# re.search() looks for the given pattern anywhere in the text.
# If the pattern exists, search() returns a match object.
# If it does not exist, it returns None.

# Real-Life Use:
# Regular expressions are useful for searching, validating, extracting, and modifying text.