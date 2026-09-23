# A Program to match one or more occurrences

import re

text = "ct cat caat caaat"

pattern = r"ca+t"

matches = re.findall(pattern, text)

print("Matches:", matches)


# Explanation:
# The + quantifier means one or more occurrences of the character immediately before it.

# In ca+t:
# c -> must appear
# a+ -> one or more "a" characters
# t -> must appear

# Therefore:
# ct     -> does NOT match because there is no "a"
# cat    -> matches
# caat   -> matches
# caaat  -> matches

# The + quantifier requires at least one occurrence.

# Real-Life Use:
# + is useful when input must contain at least one character, digit, or repeated element.