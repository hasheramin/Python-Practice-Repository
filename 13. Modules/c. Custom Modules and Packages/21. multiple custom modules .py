# A Program to use multiple custom modules

import math_operations 
import text_operations 

print("Addition:", math_operations.add(10, 5))
print("Multiplication:", math_operations.multiply(10, 5))

message = "Python Modules Are Really Useful."

print("Uppercase:", text_operations.uppercase(message))
print("Word count:", text_operations.word_count(message))

# Explanation:
# Two separate custom modules are created for different responsibilities.
# math_operations handles mathematical operations.
# text_operations handles text-related operations.
# The main program imports and uses both modules.
# Separating responsibilities makes programs easier to maintain.

# Real-Life Use:
# Large applications commonly divide functionality into separate modules instead of putting everything in one file.