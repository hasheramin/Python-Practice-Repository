# A Program to find all matches using finditer()

import re

text = "Python, Java, Python, C++"

pattern = r"Python"

matches = re.finditer(pattern, text)

for match in matches:
    print("Match:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
    print()


# Explanation:
# re.finditer() finds all occurrences of a pattern.
# Unlike findall(), finditer() returns match objects one at a time.

# Each match object provides methods such as:
# group()
# start()
# end()
# This makes finditer() useful when we need information about every match.

# Real-Life Use:
# finditer() can be used when searching documents and tracking the exact location of every match.