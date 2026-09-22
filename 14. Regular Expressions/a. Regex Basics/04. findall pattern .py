# A Program to find all occurrences of a pattern

import re

text = "Python is easy. Python is powerful. Python is popular."
pattern = "Python"

matches = re.findall(pattern, text)

print("Matches:", matches)
print("Number of matches:", len(matches))

# Explanation:
# re.findall() searches the complete text.
# Instead of returning only the first match, it returns all matching occurrences as a list.
# len() tells us how many matches were found.

# Real-Life Use:
# findall() is useful for extracting repeated information such as words, numbers, IDs, or keywords from text.