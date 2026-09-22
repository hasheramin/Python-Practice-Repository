# A Program to avoid circular imports by separating responsibilities

from user import User
from display import display_user

user = User("Hasher")

display_user(user)

# Explanation:
# user.py is responsible only for the User class.
# display.py is responsible only for displaying a user.
# The main program connects both modules.
# Neither module needs to import the other module.
# This avoids a circular dependency.

# Real-Life Use:
# Separating responsibilities helps prevent circular imports and keeps larger applications easier to maintain.