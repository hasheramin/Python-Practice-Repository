# A Program to access module-level variables by importing a module

import application

print("Application:", application.application_name)
print("Version:", application.version)
print("Running:", application.is_running)

# Explanation:
# Variables defined directly inside a module are module-level variables.
# They belong to the module and can be accessed through its name.
# Other modules can import and use these shared values.

# Real-Life Use:
# Module-level variables can hold configuration values, constants, application state, or shared settings.