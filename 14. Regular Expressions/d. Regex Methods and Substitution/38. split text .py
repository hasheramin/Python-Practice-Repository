# A Program to split text using a regular expression

import re

text = "Python,Java,C++,Go"

pattern = r","

languages = re.split(pattern, text)

print("Languages:", languages)


# Explanation:
# re.split() divides a string wherever the regular expression matches.
# The comma is used as the separator here.
# The result is a list containing the individual language names.

# Real-Life Use:
# re.split() can be useful when processing comma-separated or specially formatted text.