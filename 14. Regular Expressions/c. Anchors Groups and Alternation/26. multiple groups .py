# A Program to capture multiple groups

import re

text = "Date: 21-09-2026"

pattern = r"(\d{2})-(\d{2})-(\d{4})"

match = re.search(pattern, text)

if match:
    print("Complete date:", match.group(0))
    print("Day:", match.group(1))
    print("Month:", match.group(2))
    print("Year:", match.group(3))


# Explanation:
# The pattern contains three capturing groups.
# (\d{2}) captures the day.
# (\d{2}) captures the month.
# (\d{4}) captures the year.
# Each group receives its own number.

# group(0) -> complete match
# group(1) -> first group
# group(2) -> second group
# group(3) -> third group
# This allows us to break one matched value into separate pieces.

# Real-Life Use:
# Multiple groups are useful when extracting structured dates, phone numbers, names, or IDs.