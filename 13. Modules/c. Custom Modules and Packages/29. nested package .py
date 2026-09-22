# A Program to import a class from a nested package

from company.employees.employee import Employee

employee = Employee("Hasher", "Pookie Developer")

employee.display_info()

# Explanation:
# company is the main package.
# employees is a package inside company.
# employee.py contains the Employee class.
# The class is imported using the complete package path.

# Real-Life Use:
# Nested packages are useful for large applications where modules need to be organized into multiple categories.