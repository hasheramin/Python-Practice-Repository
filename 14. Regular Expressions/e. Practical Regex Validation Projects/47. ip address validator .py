# A Program to validate a simple IPv4 address format

import re

ip_address = "192.168.1.10"

pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

if re.fullmatch(pattern, ip_address):
    print("Valid IPv4 format.")
else:
    print("Invalid IPv4 format.")


# Explanation:
# \d{1,3} matches one to three digits.
# \. matches a literal dot.
# (\.\d{1,3}){3} means the dot-and-number section must appear exactly three times.
# Therefore the pattern expects four numeric sections separated by dots.

# Important:
# This checks the basic structure only.
# It does not ensure that every section is between 0 and 255.

# Real-Life Use:
# IP format checking can be useful when processing network configuration or user-provided addresses.