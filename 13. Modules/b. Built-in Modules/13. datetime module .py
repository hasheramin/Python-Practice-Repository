# A Program to work with dates and times

from datetime import datetime

current_time = datetime.now()

print("Current date and time:", current_time)
print("Date:", current_time.date())
print("Time:", current_time.time())
print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)

# Explanation:
# datetime.now() gets the current local date and time.
# The returned object contains separate date and time information.
# We can access individual values such as year, month, and day.

# Real-Life Use:
# Date and time handling is used in attendance systems, logs, appointments, invoices, reports, and scheduling systems.