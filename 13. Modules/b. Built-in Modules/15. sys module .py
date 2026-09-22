# A Program to access Python runtime information using sys

import sys

print("Python version:")
print(sys.version)

print("\nPython executable:")
print(sys.executable)

print("\nPlatform:")
print(sys.platform)

# Explanation:
# The sys module provides information about the Python runtime.
# version contains information about the installed Python version.
# executable shows the path of the Python interpreter.
# platform provides information about the current platform.

# Real-Life Use:
# sys is useful for command-line programs, environment checks, debugging, and interpreter information.