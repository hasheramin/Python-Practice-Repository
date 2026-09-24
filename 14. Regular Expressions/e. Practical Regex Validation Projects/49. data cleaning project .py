# A Program to clean and normalize user-provided text

import re

text = """
  Hello!!!   My email is HASHER@EXAMPLE.COM.
  Contact me at 0300-1234567.
"""

# Convert email to lowercase
text = re.sub(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    lambda match: match.group().lower(),
    text,
)

# Normalize phone number
text = re.sub(
    r"03\d{2}-\d{7}",
    lambda match: match.group().replace("-", ""),
    text,
)

# Remove extra whitespace
text = re.sub(r"\s+", " ", text)

# Remove punctuation except @ and .
text = re.sub(r"[^\w\s@.]", "", text)

# Remove leading and trailing whitespace
text = text.strip()

print("Cleaned text:")
print(text)


# Explanation:
# This project combines several regex techniques.
# First, an email pattern finds the email address and converts it to lowercase.
# Next, the phone pattern finds a phone number containing a hyphen and removes the hyphen.
# \s+ then finds repeated whitespace and replaces it with one normal space.
# [^\w\s@.] removes unwanted punctuation while preserving word characters, spaces, @, and dots.
# Finally, strip() removes whitespace from both ends.
# This demonstrates how multiple regex operations can form a simple text-cleaning pipeline.

# Real-Life Use:
# Text normalization is useful in data preprocessing, form processing, search systems, and data analysis.