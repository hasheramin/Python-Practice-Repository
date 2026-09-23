# A Program to find non-word characters

import re

text = "Hello, World!"

pattern = r"\W"

matches = re.findall(pattern, text)

print("Non-word characters:", matches)


# Explanation:
# \W represents any character that is NOT a word character.
# Punctuation marks and spaces are common examples.
# In this example, the comma, space, and exclamation mark are matched by \W.
# \W is useful when we need to detect separators or special characters.

# Real-Life Use:
# Non-word characters can be used when cleaning text or identifying punctuation and separators.