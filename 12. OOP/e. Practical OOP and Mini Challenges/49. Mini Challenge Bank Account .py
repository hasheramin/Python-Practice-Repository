# A Program to build a bank account using OOP concepts

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs. {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: Rs. {amount}")
        else:
            print("Invalid withdrawal.")

    def show_balance(self):
        print(f"{self.owner}'s Balance: Rs. {self.__balance}")


account = BankAccount("Hasher", 10000)

account.show_balance()
account.deposit(5000)
account.withdraw(3000)
account.show_balance()


# Explanation:
# BankAccount stores the owner's name and a private-like balance.
# deposit() and withdraw() control how the balance changes.
# The balance is not modified directly from outside the class.
# The program demonstrates classes, objects, encapsulation, instance methods, and validation together.

# Real-Life Use:
# This is a simplified model of a banking account and can be extended with transfers, transaction history, and account types.