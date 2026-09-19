# A Program to define addition behavior for custom objects

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"Rs. {self.amount}"


money1 = Money(500)
money2 = Money(300)

total = money1 + money2

print(total)


# Explanation:
# Money objects store an amount.
# __add__() defines what should happen when two Money objects are combined using the + operator.
# A new Money object is created with the combined amount.
# __str__() then provides a readable representation of the result.

# Real-Life Use:
# Operator overloading can make custom data types easier to use, such as money, vectors, dates, measurements, or coordinates.