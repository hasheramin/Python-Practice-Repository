# A Program to use constants from a custom module

import app_config

print("Application:", app_config.APP_NAME)
print("Version:", app_config.APP_VERSION)
print("Maximum users:", app_config.MAX_USERS)
print("Language:", app_config.DEFAULT_LANGUAGE)

# Explanation:
# Constants are stored in a separate configuration module.
# Python commonly uses uppercase names for values that are intended to remain unchanged.
# The main program accesses them through app_config.

# Real-Life Use:
# Configuration modules can store application settings, limits, default values, and other shared constants.