# A Program to clean text using multiple regular expressions

import re

text = "  Hello!!!   Python   World...  "

# Remove extra spaces
text = re.sub(r"\s+", " ", text)

# Remove punctuation
text = re.sub(r"[^\w\s]", "", text)

# Remove leading and trailing spaces
text = text.strip()

print("Cleaned text:", text)


# Explanation:
# First, \s+ finds one or more whitespace characters and replaces them with a single space.
# Next, [^\w\s] matches characters that are NOT word characters and NOT whitespace.

# This removes punctuation such as:
# !
# .
# ,

# Finally, strip() removes spaces from the beginning and end of the string.
# Multiple regex operations can be combined to build a simple text-cleaning process.

# Real-Life Use:
# Text cleaning is commonly used before analyzing user input, documents, reviews, and other text data.