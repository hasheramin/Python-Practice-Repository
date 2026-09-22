# A Program to use raw strings with regular expressions

import re

text = "Python\tProgramming"

pattern = r"\t"

result = re.search(pattern, text)

if result:
    print("Tab character found.")
else:
    print("Tab character not found.")

# Explanation:
# Regular expressions frequently use backslashes for special pattern characters.
# Raw strings prevent Python from interpreting the backslash before the regex engine receives the pattern.
# r"\t" therefore passes the pattern directly to regex.

# Real-Life Use:
# Raw strings make regular expression patterns easier to write and understand, especially for complex patterns.