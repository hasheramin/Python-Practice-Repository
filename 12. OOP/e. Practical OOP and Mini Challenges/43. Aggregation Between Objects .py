# A Program to demonstrate aggregation between classes

# In aggregation, one class contains a reference to another class, but the contained class can exist independently.

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching.")


class School:
    def __init__(self, teacher):
        self.teacher = teacher

    def start_class(self):
        self.teacher.teach()


teacher = Teacher("Hasher Amin")
school = School(teacher)

school.start_class()


# Explanation:
# The Teacher object is created independently from School.
# The existing Teacher object is then passed into School.
# School uses that object but does not create it itself.
# This represents aggregation, where objects have a relationship while remaining independently created.

# Real-Life Use:
# Aggregation is useful when objects can exist independently, such as teachers belonging to a school or employees belonging to a company.