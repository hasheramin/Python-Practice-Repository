# A Program to inspect and modify the Python module search path for custom module locations

import sys

print("Original search path:")
for path in sys.path:
    print(path)

custom_path = "custom_modules"

if custom_path not in sys.path:
    sys.path.append(custom_path)

print("\nUpdated search path:")
for path in sys.path:
    print(path)

# Explanation:
# sys.path is a Python list containing module search locations.
# A new directory can be added to this list at runtime.
# Python can then search that directory when importing modules.
# This should be used carefully because project structure is normally a better solution than modifying sys.path manually.

# Real-Life Use:
# sys.path can be useful when working with custom module locations, development environments, and debugging import problems.