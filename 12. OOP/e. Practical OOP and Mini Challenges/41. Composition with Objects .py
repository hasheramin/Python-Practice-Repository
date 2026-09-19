# A Program to demonstrate composition between classes

class Engine:
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started.")


car = Car()

car.start()


# Explanation:
# The Car class creates an Engine object inside its __init__() method.
# The engine becomes a part of the Car object.
# When car.start() runs, it uses the Engine object's start() method.
# This relationship is called composition because Car contains Engine.

# Real-Life Use:
# Composition is useful when an object is naturally built from other objects, such as a car containing an engine.