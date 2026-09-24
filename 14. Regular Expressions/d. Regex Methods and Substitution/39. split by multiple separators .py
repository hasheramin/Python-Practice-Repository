# A Program to split text using multiple separators

import re

text = "Python,Java;C++|Go"

pattern = r"[,;|]"

languages = re.split(pattern, text)

print("Languages:", languages)


# Explanation:
# The character class [,;|] matches:
# comma
# semicolon
# vertical bar

# re.split() uses any of these characters as a separator.
# This allows us to split text even when different separators are used.

# Real-Life Use:
# This is useful when processing inconsistent data received from different sources.