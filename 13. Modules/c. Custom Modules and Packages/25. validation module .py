# A Program to validate user information using a module

import validators

username = "Hasher"
age = 20
email = "hasher@example.com"

print("Valid username:", validators.is_valid_username(username))
print("Valid age:", validators.is_valid_age(age))
print("Valid email:", validators.is_valid_email(email))

# Explanation:
# Validation functions are kept inside validators.py
# The main program sends user data to these functions. Each function returns True or False.
# This keeps validation logic separate from the main application.

# Real-Life Use:
# Validation modules are useful in registration forms, login systems, APIs, databases, and web applications.