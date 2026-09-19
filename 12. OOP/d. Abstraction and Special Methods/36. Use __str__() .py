# A Program to customize the string representation of an object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"


student = Student("Ali", 20)

print(student)


# Explanation:
# __str__() is a special method called when an object is converted to a readable string, such as when it is passed to print().
# Instead of Python's default object representation, our method returns useful student information.

# Real-Life Use:
# __str__() makes objects easier to understand when displaying records, debugging programs, or printing application data.