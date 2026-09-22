# A Program to demonstrate the main guard

def greet(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet("Hasher")

# Explanation:
# The greet() function can be reused when this file is imported.
# The if __name__ == "__main__" block runs only when this file is executed directly.
# If another file imports this module, the main block does not run.
# This allows one file to work as both a module and a program.

# Real-Life Use:
# The main guard is commonly used in reusable Python modules, command-line applications, scripts, and testing code.