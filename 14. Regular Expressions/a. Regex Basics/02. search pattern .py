# A Program to search for a pattern inside text

import re

text = "I am learning Python programming."
pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
    print("Start position:", result.start())
    print("End position:", result.end())
else:
    print("Pattern not found.")

# Explanation:
# re.search() searches the complete string for a pattern.
# group() returns the matched text.
# start() returns the starting index of the match.
# end() returns the position immediately after the match.

# Real-Life Use:
# Pattern positions are useful when building text editors, search tools, and document processors.