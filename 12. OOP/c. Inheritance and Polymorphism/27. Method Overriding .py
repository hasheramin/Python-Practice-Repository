# A Program to override a parent class method

class Animal:
    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")


animal = Animal()
dog = Dog()

animal.speak()
dog.speak()


# Explanation:
# Animal defines a speak() method.
# Dog inherits from Animal but provides its own speak() method.
# The Dog version replaces the inherited behavior when called through a Dog object. This behavior is called method overriding.

# Real-Life Use:
# Overriding allows specialized classes to provide their own implementation of behavior inherited from a parent class.