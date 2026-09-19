# A Program to customize the length of an object

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)


cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

print(f"Items in cart: {len(cart)}")


# Explanation:
# ShoppingCart stores its products inside the items list.
# __len__() defines what len(cart) should return.
# Python automatically calls __len__() when len(cart) is used.
# The method returns the number of items currently in the cart.

# Real-Life Use:
# Special methods can make custom objects behave naturally with Python's built-in operations and functions.