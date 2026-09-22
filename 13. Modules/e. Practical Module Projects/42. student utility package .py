# A Program to build a student utility system using a package

from student_tools import Student, calculate_percentage, get_grade

student = Student("Hasher", 101)
marks = [85, 78, 92, 88, 76]

student.display()

percentage = calculate_percentage(marks)
grade = get_grade(percentage)

print("Percentage:", percentage)
print("Grade:", grade)

# Explanation:
# The student_tools package separates student information from result calculations.
# Student handles student data.
# result.py handles percentage and grade calculations.
# The main program combines both parts.

# Real-Life Use:
# Educational applications can use separate modules for students, courses, grades, attendance, and reports.