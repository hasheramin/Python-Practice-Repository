# A Program to search for text without considering letter case

import re

text = "Python is popular. PYTHON is powerful."
pattern = "python"

matches = re.findall(pattern, text, re.IGNORECASE)

print("Matches:", matches)
print("Number of matches:", len(matches))

# Explanation:
# Normally regex matching is case-sensitive.
# re.IGNORECASE makes the search case-insensitive.
# Therefore Python, python, and PYTHON can all match.
# findall() returns every matching occurrence.

# Real-Life Use:
# Case-insensitive searching is useful for usernames, commands, search systems, and user input.