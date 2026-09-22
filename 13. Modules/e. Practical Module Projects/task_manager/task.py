# A Program to create a task class for a task management application

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

    def display(self):
        status = "Completed" if self.completed else "Pending"
        print(f"{self.title} - {status}")
