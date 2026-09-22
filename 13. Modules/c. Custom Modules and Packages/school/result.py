# A Program to calculate student results for a custom module

def calculate_percentage(marks):
    total_marks = sum(marks)
    return total_marks / len(marks)


def get_result(percentage):
    if percentage >= 50:
        return "Pass"

    return "Fail"