# A Program to work with a regular expression match object

import re

text = "Python is powerful."

pattern = r"Python"

match = re.search(pattern, text)

if match:
    print("Match found.")
    print("Matched text:", match.group())
    print("Starting position:", match.start())
    print("Ending position:", match.end())
else:
    print("No match found.")


# Explanation:
# re.search() returns a match object when a pattern is successfully found.
# group() returns the matched text.
# start() returns the starting index.
# end() returns the ending index.
# A match object gives us more information than simply knowing whether a pattern exists.

# Real-Life Use:
# Match objects are useful when we need both the matched data and its exact location in a string.