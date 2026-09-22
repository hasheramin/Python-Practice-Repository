# A Program to use module-level functions

import user_utils

username = user_utils.create_username("Hasher", "Amin")

print("Username:", username)
print("Valid:", user_utils.is_valid_username(username))

# Explanation:
# Functions defined directly inside a module are module-level functions.
# They can be imported and reused by other Python files.
# The main program calls functions through the module name.

# Real-Life Use:
# Module-level functions are useful for utility operations, data processing, validation, formatting, and business logic.