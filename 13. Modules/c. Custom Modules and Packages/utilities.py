# A Program to create reusable utility functions for various operations

def is_even(number):
    return number % 2 == 0


def calculate_percentage(value, total):
    if total == 0:
        return 0

    return (value / total) * 100


def format_name(first_name, last_name):
    return f"{first_name.strip().title()} {last_name.strip().title()}"