# A Program to use a reusable temperature module for converting between Celsius and Fahrenheit

import temperature

celsius = 30

temperature.display_temperature(celsius)
fahrenheit = 86
converted = temperature.fahrenheit_to_celsius(fahrenheit)

print("\nConverted Celsius:", converted)

# Explanation:
# The temperature module contains related temperature functions.
# Each function has one clear responsibility.
# The main guard allows temperature.py to run directly without affecting programs that import it.
# The main program reuses the module's functions.

# Real-Life Use:
# Reusable modules are a foundation of maintainable software. Separating related functionality makes code easier to test, reuse, maintain, and expand.