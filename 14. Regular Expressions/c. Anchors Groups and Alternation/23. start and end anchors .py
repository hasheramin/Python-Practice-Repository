# A Program to validate a complete string using anchors

import re

username = "Hasher123"

pattern = r"^[A-Za-z0-9]+$"

match = re.search(pattern, username)

if match:
    print("Valid username.")
else:
    print("Invalid username.")


# Explanation:
# ^ means the pattern must start at the beginning.
# $ means the pattern must end at the end.
# [A-Za-z0-9] allows uppercase letters, lowercase letters, and digits.
# + means one or more allowed characters.

# Together:
# ^[A-Za-z0-9]+$ means the entire string must contain only letters and digits.
# This is different from searching for a valid part somewhere inside the string.

# Real-Life Use:
# Anchors are very useful when validating complete usernames, IDs, codes, and other structured input.