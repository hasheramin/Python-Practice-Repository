# A Program to search for a special character using regex

import re

text = "The price is $500."
pattern = r"\$500"

result = re.search(pattern, text)

if result:
    print("Price found:", result.group())
else:
    print("Price not found.")

# Explanation:
# Some characters have special meanings in regex.
# The dollar sign is one such character.
# A backslash is used to escape it when we want to match the actual dollar sign.
# Therefore \$ represents a literal dollar sign.

# Real-Life Use:
# Escaping special characters is important when searching for symbols such as $, ., +, *, ?, (, and ).