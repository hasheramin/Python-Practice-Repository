# A Program to create an employee module inside a nested package for a company

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print("Name:", self.name)
        print("Position:", self.position)