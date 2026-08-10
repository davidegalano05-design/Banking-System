from abc import ABC, abstractmethod
from transaction import Transaction

class Account(ABC):
    def __init__(self, account_number, owner_name, pin, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.pin = str(pin)
        self.balance = balance
        self.transaction_history = []

    def verify_pin(self, input_pin):
        return self.pin == str(input_pin)

    def deposit(self, amount):
        if amount <= 0:
            return (False, "Deposit amount must be positive.")
        else:
            self.balance += amount
            transaction = Transaction("deposit", amount, self)
            self.transaction_history.append(transaction)
            return (True, f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    @abstractmethod
    def withdraw(self, amount,input_pin):
        pass

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history