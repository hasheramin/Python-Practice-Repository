# A Program to group multiple characters together

import re

text = "ha ha ha hello"

pattern = r"(ha)+"

matches = re.findall(pattern, text)

print("Matches:", matches)


# Explanation:
# Parentheses () create a group.
# (ha) treats "ha" as one unit.
# The + quantifier is then applied to the complete group instead of only one character.

# Therefore (ha)+ means:
# one or more repetitions of "ha".
# Grouping allows us to apply quantifiers to multiple characters together.

# Real-Life Use:
# Groups are useful when repeated patterns contain more than one character.