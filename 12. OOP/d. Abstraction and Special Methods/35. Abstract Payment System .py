# A Program to create multiple implementations of an abstract class

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using card.")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using cash.")


class OnlinePayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using online payment.")


payments = [
    CardPayment(),
    CashPayment(),
    OnlinePayment()
]

for payment in payments:
    payment.pay(1000)


# Explanation:
# Payment defines the required pay() method.
# Each child class provides a different implementation.
# The payments list stores objects of different payment classes.
# The loop calls the same method while each object performs its own payment behavior.

# Real-Life Use:
# Payment systems can support cards, cash, wallets, and online providers while following the same basic payment interface.