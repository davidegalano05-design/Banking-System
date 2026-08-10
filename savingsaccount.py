from account import Account
from transaction import Transaction

class SavingsAccount(Account):
    def __init__(self, account_number, owner_name, pin, balance=0, interest_rate=0.01, min_balance=100):
        super().__init__(account_number, owner_name, pin, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def withdraw(self, amount, input_pin):
        if not self.verify_pin(input_pin):
            return (False, "Invalid PIN.")
        if amount <= 0:
            return (False, "Withdrawal amount must be positive.")
        elif (self.balance - amount) < self.min_balance:
            return (False, f"Cannot withdraw ${amount:.2f}. Minimum balance of ${self.min_balance:.2f} must be maintained.")
        else:
            self.balance -= amount
            transaction = Transaction("withdrawal", amount, self)
            self.transaction_history.append(transaction)
            return (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        transaction = Transaction("interest", interest_amount, self)
        self.transaction_history.append(transaction)
        return (True, f"Applied interest of ${interest_amount:.2f}. New balance: ${self.balance:.2f}")