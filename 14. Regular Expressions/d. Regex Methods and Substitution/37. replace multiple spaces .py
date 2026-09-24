# A Program to replace multiple spaces with one space

import re

text = "Python    is     easy     to learn."

pattern = r"\s+"

new_text = re.sub(pattern, " ", text)

print("Original:", text)
print("Cleaned:", new_text)


# Explanation:
# \s matches whitespace characters.
# + means one or more whitespace characters.
# Therefore \s+ finds groups of one or more spaces or other whitespace characters.
# re.sub() replaces each group with one normal space.
# This produces cleaner and more consistent text.

# Real-Life Use:
# This is useful when cleaning text copied from documents, websites, or user input.