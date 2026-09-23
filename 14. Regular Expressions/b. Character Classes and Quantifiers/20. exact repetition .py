# A Program to match an exact number of repetitions

import re

text = "123 1234 12345 12"

pattern = r"\d{3}"

matches = re.findall(pattern, text)

print("Three-digit sequences:", matches)


# Explanation:
# {3} means exactly three occurrences of the element before it.

# In \d{3}:
# \d -> digit
# {3} -> exactly three digits

# Therefore:
# 123   -> matches
# 1234  -> contains a matching three-digit sequence
# 12345 -> contains a matching three-digit sequence
# 12    -> does not contain three digits

# Curly braces can also define ranges, such as:
# \d{2,4}
# This means two to four digits.


# Real-Life Use:
# Exact repetition is useful for fixed-length codes, PINs, IDs, and structured numeric input.