# A Program to validate a simple URL

import re

url = "https://www.example.com"

pattern = r"^https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, url):
    print("Valid URL format.")
else:
    print("Invalid URL format.")


# Explanation:
# https? means:
# http
# or
# https

# The ? makes the "s" optional.
# :// matches the standard URL separator.
# [A-Za-z0-9.-]+ matches the domain portion.
# \. matches the dot before the domain extension.
# [A-Za-z]{2,} matches the extension.
# This is a simplified URL format validator, not a complete URL specification.

# Real-Life Use:
# URL validation can be useful when accepting website addresses from users.