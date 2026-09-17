# A Program to use super() with inheritance

class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


developer = Developer("Hasher", "Python")

print(f"Name: {developer.name}")
print(f"Language: {developer.language}")


# Explanation:
# Employee initializes the name attribute.
# Developer has its own __init__() because it needs language as well.
# super().__init__(name) calls the parent class constructor.
# Developer then initializes its additional language attribute.

# Real-Life Use:
# super() is useful when a child class extends the initialization or behavior of a parent class without duplicating its code.