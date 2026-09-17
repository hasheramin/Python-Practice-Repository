# A Program to extend a parent method using super()

class Employee:
    def show_details(self):
        print("Employee works at the company.")


class Developer(Employee):
    def show_details(self):
        super().show_details()
        print("Developer specializes in software development.")


developer = Developer()

developer.show_details()


# Explanation:
# Employee provides the original show_details() method.
# Developer overrides that method.
# super().show_details() calls the parent implementation first.
# Developer then adds its own specialized information.

# Real-Life Use:
# This pattern is useful when a child class needs to keep parent behavior while adding extra functionality.