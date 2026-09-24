# A Program to replace text using re.sub()

import re

text = "I like Java. Java is popular."

pattern = r"Java"

replacement = "Python"

new_text = re.sub(pattern, replacement, text)

print("Original:", text)
print("Updated:", new_text)


# Explanation:
# re.sub() replaces every occurrence of a pattern with the provided replacement text.
# Here, every occurrence of Java is replaced with Python.
# The original string is not changed directly.
# re.sub() returns a new string.

# Real-Life Use:
# re.sub() is useful for replacing words, correcting text, and modifying structured data.