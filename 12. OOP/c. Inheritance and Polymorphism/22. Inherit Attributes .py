# A Program to inherit attributes from a parent class

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving.")


car = Car("Toyota")

print(car.brand)
car.drive()


# Explanation:
# Vehicle defines the brand attribute inside __init__().
# Car inherits from Vehicle. When Car creates an object, the inherited initializer stores brand. The drive() method then accesses that inherited attribute.

# Real-Life Use:
# A parent class can define shared data for related objects, such as brand and model information for different vehicles.