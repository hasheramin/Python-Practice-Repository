# A Program to create a simple inventory management system

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_details(self):
        print(f"{self.name} - Rs. {self.price} - Quantity: {self.quantity}")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_inventory(self):
        for product in self.products:
            product.show_details()


product1 = Product("Laptop", 100000, 5)
product2 = Product("Mouse", 2000, 20)

inventory = Inventory()

inventory.add_product(product1)
inventory.add_product(product2)

inventory.show_inventory()


# Explanation:
# Product stores information about an individual product.
# Inventory maintains a collection of Product objects.
# Products are created separately and added to the inventory.
# show_inventory() asks each Product to display its own information.

# Real-Life Use:
# Inventory systems use this structure to manage products, stock quantities, prices, and warehouse information.