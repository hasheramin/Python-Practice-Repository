# A Program to demonstrate multilevel inheritance

class Animal:
    def eat(self):
        print("Animal is eating.")


class Mammal(Animal):
    def walk(self):
        print("Mammal is walking.")


class Dog(Mammal):
    def bark(self):
        print("Dog is barking.")


dog = Dog()

dog.eat()
dog.walk()
dog.bark()


# Explanation:
# Animal is the first level of the inheritance chain.
# Mammal inherits from Animal.
# Dog then inherits from Mammal.
# Dog therefore gets access to methods from both parent levels.

# Real-Life Use:
# Multilevel inheritance can model layered relationships, such as Device to Computer and then to Laptop.