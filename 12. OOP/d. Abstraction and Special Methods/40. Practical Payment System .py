# A Program to build a practical polymorphic payment system

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Card payment successful: Rs. {amount}")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Cash payment successful: Rs. {amount}")


class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Wallet payment successful: Rs. {amount}")


def process_payment(payment, amount):
    payment.pay(amount)


payments = [
    CardPayment(),
    CashPayment(),
    WalletPayment()
]

for payment in payments:
    process_payment(payment, 2500)


# Explanation:
# Payment defines the common pay() interface using an abstract method.
# Each payment class implements pay() differently.
# process_payment() accepts any object that follows the Payment interface.
# The loop processes different payment objects using the same function.

# This all combines abstraction, inheritance, and polymorphism.

# Real-Life Use:
# Real payment systems can support multiple payment providers while keeping the main payment-processing logic independent from each individual payment method.