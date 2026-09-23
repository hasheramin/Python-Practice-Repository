# A Program to extract username and domain from an email

import re

email = "hasher@example.com"

pattern = r"^(\w+)@(\w+)\.(\w+)$"

match = re.search(pattern, email)

if match:
    print("Email:", match.group(0))
    print("Username:", match.group(1))
    print("Domain:", match.group(2))
    print("Extension:", match.group(3))
else:
    print("Invalid email format.")


# Explanation:
# ^ ensures that matching starts at the beginning.
# (\w+) captures the username.
# @ matches the @ symbol literally.
# (\w+) captures the domain name.
# \. matches a literal dot.
# The dot must be escaped because . has a special meaning in regular expressions.
# (\w+) captures the domain extension.
# $ ensures that matching ends at the end of the string.
# The complete pattern therefore validates and extracts different parts of a simple email address.

# Real-Life Use:
# Groups, anchors, and alternation are useful for extracting structured information from user input.