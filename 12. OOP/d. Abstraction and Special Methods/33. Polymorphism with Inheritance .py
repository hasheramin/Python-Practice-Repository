# A Program to demonstrate polymorphism through inheritance

class Animal:
    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")


animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()


# Explanation:
# Dog and Cat inherit from Animal and override speak().
# The list contains objects from different classes.
# The loop calls the same speak() method on every object.
# Each object executes the implementation belonging to its class.

# Real-Life Use:
# Polymorphism makes systems easier to extend because new child classes can provide their own behavior without changing the loop.