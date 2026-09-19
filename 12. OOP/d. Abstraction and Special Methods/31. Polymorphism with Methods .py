# A Program to demonstrate polymorphism with different classes

class Dog:
    def speak(self):
        print("Dog says: Woof!")


class Cat:
    def speak(self):
        print("Cat says: Meow!")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# Explanation:
# Dog and Cat are separate classes. Both classes have a method with the same name: speak(). Each object provides its own implementation of that method. The same method name can therefore produce different behavior.

# Real-Life Use:
# Polymorphism allows different objects to respond to the same operation in their own way, which is common in large applications.