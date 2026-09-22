# A Program to use a date utility module for date manipulation and formatting

import date_utils

today = date_utils.current_date()
future_date = date_utils.days_from_today(30)

print("Today:", date_utils.format_date(today))
print("After 30 days:", date_utils.format_date(future_date))

# Explanation:
# date_utils.py contains reusable date-related functions.
# current_date() gets today's date.
# days_from_today() calculates a future date.
# format_date() converts a date into a readable format.

# Real-Life Use:
# Date utilities are useful for appointments, deadlines, subscriptions, invoices, and scheduling systems.