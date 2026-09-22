# A Program to access variables from a custom module for settings

import settings

print("Application:", settings.app_name)
print("Version:", settings.version)
print("Developer:", settings.developer)

# Explanation:
# The settings module contains variables.
# After importing the module, those variables can be accessed using the module name followed by the variable name.
# This allows configuration data to stay separate from main code.

# Real-Life Use:
# Configuration values such as application name, version, database settings, and constants can be stored inside dedicated modules.