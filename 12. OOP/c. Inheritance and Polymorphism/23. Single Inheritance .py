# A Program to demonstrate single inheritance

class Employee:
    def show_role(self):
        print("Employee works for the company.")


class Developer(Employee):
    def write_code(self):
        print("Developer writes code.")


developer = Developer()

developer.show_role()
developer.write_code()


# Explanation:
# Employee is the parent class.
# Developer is the child class and inherits from Employee. This is called single inheritance because one child class directly inherits from one parent class. Developer can use both its own and inherited methods.

# Real-Life Use:
# Single inheritance is useful when a specialized class extends the behavior of one general class.