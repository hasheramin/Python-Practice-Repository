# A Program to create a module-level class

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)