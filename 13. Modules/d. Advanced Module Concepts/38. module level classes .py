# A Program to use a class defined inside a module

from product import Product

product = Product("Keyboard", 5000)

product.display()

# Explanation:
# Product is defined directly inside the product module.
# The class is imported into the main program.
# An object is created using the imported class.
# Its method is then called normally.

# Real-Life Use:
# Real applications often place related classes inside modules such as models, services, database objects, and controllers.