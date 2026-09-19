# A Program to use polymorphism through a common function

class Dog:
    def speak(self):
        print("Dog says: Woof!")


class Cat:
    def speak(self):
        print("Cat says: Meow!")


def make_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# Explanation:
# Dog and Cat both provide a speak() method.
# make_sound() does not need to know the exact class of animal.
# It simply calls the speak() method available on the object.
# Python determines which implementation should run at runtime.

# Real-Life Use:
# This approach is useful when one function needs to work with many different object types that provide the same behavior.