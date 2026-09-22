# A Program to create a reusable temperature module for converting between Celsius and Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def display_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)

    print("Celsius:", celsius)
    print("Fahrenheit:", fahrenheit)


if __name__ == "__main__":
    display_temperature(25)