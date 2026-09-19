# A Program to compare two objects using __eq__()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


product1 = Product("Laptop", 100000)
product2 = Product("Laptop", 100000)

print(product1 == product2)


# Explanation:
# Two Product objects are created with the same data.
# __eq__() defines how two Product objects should be compared.
# It checks both name and price.
# Therefore, the objects are considered equal when both values match.

# Real-Life Use:
# Custom equality is useful when objects represent data records and equality should depend on their stored values.