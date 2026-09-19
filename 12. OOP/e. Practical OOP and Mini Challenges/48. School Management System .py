# A Program to create a simple school management system

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Student: {self.name}")


class Teacher:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Teacher: {self.name}")


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_people(self):
        print("Students:")
        for student in self.students:
            student.show()

        print("Teachers:")
        for teacher in self.teachers:
            teacher.show()


school = School()

school.add_student(Student("Ali"))
school.add_student(Student("Ayesha"))

school.add_teacher(Teacher("Mr. Hasher"))
school.add_teacher(Teacher("Ms. Amin"))

school.show_people()


# Explanation:
# Student and Teacher represent two different types of people.
# School maintains separate collections for students and teachers.
# Objects are created and then added to the School.
# show_people() uses the methods of each stored object.

# Real-Life Use:
# This structure provides a foundation for school software that can manage students, teachers, classes, and records.