# A Program to find characters using a character class

import re

text = "Python, Java, C++, Go"

pattern = r"[PJCG]"

matches = re.findall(pattern, text)

print("Matching characters:", matches)


# Explanation:
# [PJCG] creates a character class.
# It matches any ONE character that is P, J, C, or G.
# re.findall() searches the complete string and returns every character that matches the pattern.
# The square brackets are useful when we want to match one character from a specific group of characters.

# Real-Life Use:
# Character classes can be used to find specific letters, symbols, or allowed characters in user input.