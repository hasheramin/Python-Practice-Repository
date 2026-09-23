# A Program to create a non-capturing group

import re

text = "Python Java Python Java"

pattern = r"(?:Python|Java)"

matches = re.findall(pattern, text)

print("Matches:", matches)


# Explanation:
# (?:...) creates a non-capturing group.
# It groups multiple pattern elements together without creating a numbered capturing group.

# Here:
# (?:Python|Java) means match either Python or Java, but do not store the selected value as a numbered capture group.
# Non-capturing groups are useful when grouping is required but the captured value is not needed.

# Real-Life Use:
# They are useful in larger regular expressions where grouping is needed for logic but extracted group values are unnecessary.