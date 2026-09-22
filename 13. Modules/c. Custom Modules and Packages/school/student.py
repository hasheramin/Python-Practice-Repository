# A Program to create a Student class inside a package for a school

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_info(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)