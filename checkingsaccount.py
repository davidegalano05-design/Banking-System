from account import Account
from transaction import Transaction
class CheckingAccount(Account):
    def __init__(self, account_number, owner_name, pin, balance=0, overdraft_limit=100):
        super().__init__(account_number, owner_name, pin, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount, input_pin):
        if not self.verify_pin(input_pin):
            return (False, "Invalid PIN.")
        if amount <= 0:
            return (False, "Withdrawal amount must be positive.")
        elif (self.balance - amount) < -self.overdraft_limit:
            return (False, f"Cannot withdraw ${amount:.2f}. Overdraft limit of ${self.overdraft_limit:.2f} exceeded.")
        else:
            self.balance -= amount
            transaction = Transaction("withdrawal", amount, self)
            self.transaction_history.append(transaction)
            if self.balance < 0:
                return (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}. Warning: You are in overdraft.")
            else:
                return (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")