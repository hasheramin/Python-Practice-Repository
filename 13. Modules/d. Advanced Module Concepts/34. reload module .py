# A Program to reload an imported module

import counter
import importlib

print("Original value:", counter.counter)
counter.counter = 50

print("Changed value:", counter.counter)
importlib.reload(counter)

print("After reload:", counter.counter)

# Explanation:
# counter.py contains a variable named counter.
# The module is imported and its value is changed in memory.
# importlib.reload() loads the module again from its source file.
# The module's original value is restored when it is reloaded.

# Real-Life Use:
# Module reloading can be useful during development when testing changes to imported modules without restarting the entire Python process.