# A Program to demonstrate multiple inheritance

class Camera:
    def take_photo(self):
        print("Taking a photo.")


class Phone:
    def make_call(self):
        print("Making a phone call.")


class Smartphone(Camera, Phone):
    def use_apps(self):
        print("Using smartphone apps.")


phone = Smartphone()

phone.take_photo()
phone.make_call()
phone.use_apps()


# Explanation:
# Camera and Phone are two separate parent classes.
# Smartphone inherits from both classes.
# The Smartphone object can use methods from Camera and Phone, as well as its own use_apps() method.

# Real-Life Use:
# Multiple inheritance can represent a class that combines capabilities from multiple independent classes.