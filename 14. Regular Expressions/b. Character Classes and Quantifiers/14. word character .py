# A Program to find word characters

import re

text = "Python_3 is powerful!"

pattern = r"\w"

matches = re.findall(pattern, text)

print("Word characters:", matches)


# Explanation:
# \w matches word characters.
# In Python regular expressions, \w normally includes letters, digits, and underscore characters.
# re.findall() returns each matching character.
# In "Python_3", the letters, underscore, and digit are all considered word characters.

# Real-Life Use:
# \w can be useful when working with usernames, variable names, identifiers, and text tokens.