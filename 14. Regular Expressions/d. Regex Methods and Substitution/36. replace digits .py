# A Program to replace digits with a symbol

import re

text = "Order 123 contains 5 items."

pattern = r"\d+"

new_text = re.sub(pattern, "#", text)

print("Original:", text)
print("Updated:", new_text)


# Explanation:
# \d matches digits.
# + means one or more digits.
# Therefore \d+ matches complete numeric sequences such as 123 and 5.
# re.sub() replaces each numeric sequence with the # symbol.

# Real-Life Use:
# This technique can be used to hide or mask numeric information before displaying text.