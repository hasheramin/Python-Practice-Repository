# A Program to match zero or one occurrence

import re

text = "color colour"

pattern = r"colou?r"

matches = re.findall(pattern, text)

print("Matches:", matches)


# Explanation:
# The ? quantifier means zero or one occurrence of the character immediately before it.

# In colou?r:
# colo -> required
# u?   -> zero or one "u"
# r    -> required

# Therefore both:
# color
# colour
# match the pattern.
# The ? quantifier is useful when a character is optional.

# Real-Life Use:
# This can handle variations in spelling or optional parts of user input.