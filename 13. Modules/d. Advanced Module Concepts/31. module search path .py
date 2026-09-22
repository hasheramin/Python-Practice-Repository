# A Program to explore Python's module search path

import sys

print("Python searches for modules in these locations:")

for path in sys.path:
    print(path)

# Explanation:
# Python searches specific directories when importing a module.
# sys.path contains the locations Python checks.
# The current project directory is normally included.
# Python continues checking these locations until it finds the module.

# Real-Life Use:
# Understanding the module search path helps diagnose ModuleNotFoundError and import-related problems.