from datetime import datetime

class Transaction :
    def __init__(self, transaction_type, amount, account):
        self.transaction_type = transaction_type
        self.amount = amount
        self.account = account
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.timestamp}] {self.transaction_type.title()} - ${self.amount:.2f}"