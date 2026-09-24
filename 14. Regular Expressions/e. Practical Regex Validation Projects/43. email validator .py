# A Program to validate a simple email address

import re

email = "hasher@example.com"

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Valid email format.")
else:
    print("Invalid email format.")


# Explanation:
# [A-Za-z0-9._%+-]+ matches the username portion.
# @ matches the @ symbol.
# [A-Za-z0-9.-]+ matches the domain name.
# \. matches the actual dot before the extension.
# [A-Za-z]{2,} matches an extension containing at least two letters.

# This is a practical format check, not a complete verification that the email address actually exists.

# Real-Life Use:
# Email format validation is commonly used in registration forms and contact forms.