# A Program to understand __name__ in a Python module

print("Module name:", __name__)

if __name__ == "__main__":
    print("This file is being run directly.")
else:
    print("This file is being imported.")

# Explanation:
# Python gives every module a special variable called __name__.
# When a file is executed directly, __name__ becomes "__main__".
# When the file is imported, __name__ contains the module name.
# This allows us to separate reusable code from direct execution.

# Real-Life Use:
# The __name__ check is commonly used to make a Python file work both as a reusable module and as a directly executable program.