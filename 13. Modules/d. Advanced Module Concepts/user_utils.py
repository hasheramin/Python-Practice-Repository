# A Program to create module-level utility functions

def create_username(first_name, last_name):
    return f"{first_name.lower()}_{last_name.lower()}"


def is_valid_username(username):
    return len(username) >= 4