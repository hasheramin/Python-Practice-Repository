# A Program to generate random values using the random module

import random

number = random.randint(1, 100)

colors = ["Red", "Blue", "Green", "Black", "White"]
selected_color = random.choice(colors)

print("Random number:", number)
print("Random color:", selected_color)

# Explanation:
# The random module provides functions for generating random values.
# randint() generates a random integer within the given range.
# choice() randomly selects one item from a sequence.
# Every execution can produce different results.

# Real-Life Use:
# Random values are useful in games, simulations, testing, random selections, and simple experiments.