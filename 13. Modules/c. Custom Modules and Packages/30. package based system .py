# A Program to build a simple school system using a package

from school.student import Student
from school.result import calculate_percentage, get_result

student = Student("Hasher", 101)

marks = [85, 78, 90, 88, 76]

student.display_info()

percentage = calculate_percentage(marks)
result = get_result(percentage)

print("Percentage:", percentage)
print("Result:", result)

# Explanation:
# The school package contains separate modules for student information and result calculations.
# Student handles object-related data.
# result.py handles calculation and result logic.
# The main program combines both modules to build a small system.
# This demonstrates how packages help separate responsibilities.

# Real-Life Use:
# Real applications divide features into modules and packages. This makes the code easier to maintain, test, reuse, and expand.