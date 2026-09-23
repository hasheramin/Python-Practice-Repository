# A Program to capture a specific part of a pattern

import re

text = "Name: Hasher"

pattern = r"Name: (\w+)"

match = re.search(pattern, text)

if match:
    print("Complete match:", match.group(0))
    print("Captured name:", match.group(1))


# Explanation:
# Parentheses create a capturing group.
# (\w+) captures one or more word characters.
# group(0) contains the complete matched text.
# group(1) contains the first captured group.

# In this example:
# group(0) -> Name: Hasher
# group(1) -> Hasher
# Capturing groups allow us to extract useful information from a larger pattern.

# Real-Life Use:
# Capturing groups are commonly used to extract names, IDs, dates, usernames, and other data.