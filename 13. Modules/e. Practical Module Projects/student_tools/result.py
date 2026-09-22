# A Program to calculate student results

def calculate_percentage(marks):
    if not marks:
        return 0

    return sum(marks) / len(marks)


def get_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
