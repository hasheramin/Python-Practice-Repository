# A Program to extract structured information from text

import re

text = """
Name: Hasher
Email: hasher@example.com
Phone: 03001234567
"""

pattern = (
    r"Name:\s*(?P<name>\w+)\s*"
    r"Email:\s*(?P<email>[\w.-]+@[\w.-]+\.\w+)\s*"
    r"Phone:\s*(?P<phone>03\d{9})"
)

match = re.search(pattern, text)

if match:
    print("Name:", match.group("name"))
    print("Email:", match.group("email"))
    print("Phone:", match.group("phone"))
else:
    print("Information not found.")


# Explanation:
# This example combines several regex concepts.
# \s* allows optional whitespace.
# (?P<name>...) creates a named capturing group.
# Named groups make extracted information easier to understand than numeric group indexes.

# The pattern extracts:
# name
# email
# phone
# group("name"), group("email"), and group("phone") access the captured values directly.

# Real-Life Use:
# Regex extraction can be used for processing logs, documents, forms, and semi-structured data.