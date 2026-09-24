# A Program to extract data using the group method

import re

text = "User: Hasher, Age: 20"

pattern = r"User: (\w+), Age: (\d+)"

match = re.search(pattern, text)

if match:
    print("Complete match:", match.group(0))
    print("Username:", match.group(1))
    print("Age:", match.group(2))


# Explanation:
# group(0) returns the complete matched text.
# group(1) returns the first capturing group.
# group(2) returns the second capturing group.
# The pattern captures the usernam and age separately from the same string.
# Capturing groups make it possible to extract structured information from unstructured text.

# Real-Life Use:
# This can be used to extract user information, product details, IDs, or other structured values.