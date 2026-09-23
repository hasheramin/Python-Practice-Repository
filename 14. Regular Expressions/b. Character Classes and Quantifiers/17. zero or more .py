# A Program to match zero or more occurrences

import re

text = "ct cat caat caaat"

pattern = r"ca*t"

matches = re.findall(pattern, text)

print("Matches:", matches)


# Explanation:
# The * quantifier means zero or more occurrences of the character immediately before it.

# In ca*t:
# c -> must appear
# a* -> zero or more "a" characters
# t -> must appear

# Therefore:
# ct     -> matches
# cat    -> matches
# caat   -> matches
# caaat  -> matches

# The * quantifier makes the previous element optional and allows it to repeat multiple times.

# Real-Life Use:
# This is useful when a piece of text may appear zero times, once, or many times.