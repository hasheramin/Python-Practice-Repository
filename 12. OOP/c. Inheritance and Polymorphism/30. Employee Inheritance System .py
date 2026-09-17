# A Program to create a simple employee inheritance system

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


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


developer = Developer("Hasher", 90000, "Python")
designer = Designer("Amin", 85000, "Figma")

developer.show_details()
print()

designer.show_details()


# Explanation:
# Employee stores the common name and salary attributes.
# Developer and Designer inherit those attributes using super().
# Each child class adds its own specialized attribute.
# Both child classes override show_details() while still using the parent's implementation through super().

# Real-Life Use:
# This structure can model real company systems where employees share common information but different roles have specialized data.