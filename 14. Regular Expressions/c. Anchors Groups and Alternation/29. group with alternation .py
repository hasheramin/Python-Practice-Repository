# A Program to combine grouping with alternation

import re

text = "I like Python and Java."

pattern = r"I like (Python|Java)"

matches = re.findall(pattern, text)

print("Matched languages:", matches)


# Explanation:
# The parentheses create a capturing group.
# Python|Java means either Python or Java.

# Therefore:
# (Python|Java) captures whichever language matches.
# Because findall() is used with one capturing group, the result contains the captured language values.

# Real-Life Use:
# Grouped alternation is useful when extracting one value from multiple accepted choices.