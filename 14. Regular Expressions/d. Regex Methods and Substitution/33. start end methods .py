# A Program to find the position of a matched pattern

import re

text = "Learning Python is interesting."

pattern = r"Python"

match = re.search(pattern, text)

if match:
    print("Matched text:", match.group())
    print("Start index:", match.start())
    print("End index:", match.end())
else:
    print("Pattern not found.")


# Explanation:
# start() gives the index where the match begins.
# end() gives the index immediately after the match.
# Python starts at index 9 in this string.
# If the matched text has a length of 6, end() will return 15.
# The difference between end() and start() gives the length of the matched text.

# Real-Life Use:
# Positions are useful when highlighting, editing, or replacing specific portions of text.