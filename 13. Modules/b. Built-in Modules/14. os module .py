# A Program to use the os module for operating system information

import os

current_directory = os.getcwd()

print("Current directory:")
print(current_directory)

print("\nFiles and folders:")
for item in os.listdir(current_directory):
    print(item)

# Explanation:
# The os module allows Python to interact with the operating system.
# getcwd() returns the current working directory.
# listdir() returns the files and folders inside a directory.
# The loop displays each item separately.

# Real-Life Use:
# The os module is useful for file management, directory operations, automation, and system-level tasks.