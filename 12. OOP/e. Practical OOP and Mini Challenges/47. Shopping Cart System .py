# A Program to create a simple shopping cart system

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        total = 0

        for product in self.products:
            total += product.price

        return total

    def show_cart(self):
        for product in self.products:
            print(f"{product.name}: Rs. {product.price}")


product1 = Product("Laptop", 100000)
product2 = Product("Mouse", 2000)

cart = ShoppingCart()

cart.add_product(product1)
cart.add_product(product2)

cart.show_cart()
print(f"Total: Rs. {cart.total_price()}")


# Explanation:
# Product represents an item that can be purchased.
# ShoppingCart contains Product objects in its products list.
# total_price() loops through the products and calculates the total.
# The cart therefore coordinates multiple Product objects.

# Real-Life Use:
# This design can be expanded into an e-commerce system with discounts, quantities, taxes, checkout, and payment processing.