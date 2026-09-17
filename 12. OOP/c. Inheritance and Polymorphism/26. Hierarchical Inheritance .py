# A Program to demonstrate hierarchical inheritance

class Employee:
    def work(self):
        print("Employee is working.")


class Developer(Employee):
    def write_code(self):
        print("Developer is writing code.")


class Designer(Employee):
    def design(self):
        print("Designer is creating a design.")


developer = Developer()
designer = Designer()

developer.work()
developer.write_code()

designer.work()
designer.design()


# Explanation:
# Employee is the common parent class.
# Developer and Designer both inherit from Employee.
# Both child classes receive the shared work() method.
# Each child class also has its own specialized behavior.

# Real-Life Use:
# Hierarchical inheritance is useful when several roles share common functionality but also have different responsibilities.