# A Program to create validation functions for user input

def is_valid_username(username):
    return len(username) >= 4


def is_valid_age(age):
    return 18 <= age <= 100


def is_valid_email(email):
    return "@" in email and "." in email