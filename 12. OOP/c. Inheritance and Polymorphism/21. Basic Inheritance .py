# A Program to create a basic inheritance relationship

class Animal:
    def eat(self):
        print("The animal is eating.")


class Dog(Animal):
    def bark(self):
        print("The dog is barking.")


dog = Dog()

dog.eat()
dog.bark()


# Explanation:
# Animal is the parent class and contains the eat() method. Dog inherits from Animal, so Dog objects can use eat(). Dog also defines its own bark() method. The dog object can therefore use methods from both classes.

# Real-Life Use:
# Inheritance is useful when multiple classes share common behavior, such as different types of employees, vehicles, or animals.