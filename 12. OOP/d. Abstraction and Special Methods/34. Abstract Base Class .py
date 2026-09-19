# A Program to create an abstract base class

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using cash.")


payment = CashPayment()
payment.pay(500)


# Explanation:
# Payment inherits from ABC, making it an abstract base class.
# pay() is marked with @abstractmethod.
# Child classes must provide their own implementation of pay().
# CashPayment implements pay(), so its object can be created.

# Real-Life Use:
# Abstract classes are useful for defining common rules for systems such as payments, notifications, storage, or database providers.