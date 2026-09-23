# A Program to match one pattern from multiple choices

import re

text = "I use Python for development."

pattern = r"Python|Java"

match = re.search(pattern, text)

if match:
    print("Matched:", match.group())
else:
    print("No language matched.")


# Explanation:
# The | symbol means OR.
# Python|Java means: match Python OR Java.
# Since the text contains Python, the regular expression finds Python.
# Alternation allows a pattern to accept multiple possible values.

# Real-Life Use:
# Alternation is useful when input can contain one of several known options.