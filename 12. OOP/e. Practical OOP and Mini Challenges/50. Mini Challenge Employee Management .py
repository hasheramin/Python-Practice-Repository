# A Program to build an employee management system using OOP

class Employee:
    company = "Tech Solutions"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: Rs. {self.salary}")
        print(f"Company: {self.company}")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_details(self):
        super().show_details()
        print(f"Language: {self.language}")


class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    def show_details(self):
        super().show_details()
        print(f"Design Tool: {self.tool}")


employees = [
    Developer("Hasher", 90000, "Python"),
    Designer("Amin", 85000, "Figma")
]

for employee in employees:
    employee.show_details()
    print()


# Explanation:
# Employee contains common employee information.
# Developer and Designer inherit from Employee and add specialized data.
# super() reuses the parent constructor and show_details() method.
# Both child classes override show_details().
# The employees list contains different object types, demonstrating polymorphism when the same method is called inside the loop.

# Real-Life Use:
# This pattern can form the foundation of an employee management application with departments, roles, salaries, attendance, and payroll.