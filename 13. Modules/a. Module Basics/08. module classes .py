# A Program to use a class from a custom module

import student

student_one = student.Student("Hasher", 20)

student_one.display_info()

# Explanation:
# The Student class is defined inside student.py.
# The main program imports the student module.
# An object is created using student.Student().
# The object's method is then called normally.

# Real-Life Use:
# Classes can be placed inside modules to organize models, services, database objects, and application logic.