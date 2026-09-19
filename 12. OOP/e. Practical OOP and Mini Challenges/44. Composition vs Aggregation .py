# A Program to compare composition and aggregation

# In composition, one class creates and owns another class, while in aggregation, one class contains a reference to another class that can exist independently.

class Engine:
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self):
        self.engine = Engine()


class Driver:
    def __init__(self, name):
        self.name = name


class Taxi:
    def __init__(self, driver):
        self.driver = driver


car = Car()

driver = Driver("Hasher")
taxi = Taxi(driver)

car.engine.start()
print(f"Taxi driver: {taxi.driver.name}")


# Explanation:
# Car creates its Engine internally, which demonstrates composition.
# Taxi receives an already-created Driver object, which demonstrates aggregation.
# The Engine is created as part of Car, while Driver exists separately.
# These relationships help describe how objects depend on each other.

# Real-Life Use:
# Understanding these relationships helps developers design flexible systems and decide how objects should be connected.