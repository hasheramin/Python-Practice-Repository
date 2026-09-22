# A Program to find a simple email address inside text

import re

text = "Contact us at hasher@example.com for more information."
pattern = r"[\w.-]+@[\w.-]+\.\w+"
# A simple regex pattern for matching email addresses. I know it is not easy to learn these types of patterns, but you can master them with practice and patience.

result = re.search(pattern, text)

if result:
    print("Email found:", result.group())
else:
    print("Email not found.")

# Explanation:
# [\w.-]+ matches one or more letters, numbers, underscores,
# dots, or hyphens before the @ symbol.
# @ matches the email separator.
# [\w.-]+ matches the domain name.
# \.\w+ matches the dot and domain extension.
# This is a basic email pattern, not a complete email specification.

# Real-Life Use:
# Regex email patterns are commonly used for basic input validation and extracting emails from text.