import json
import os
from savingsaccount import SavingsAccount
from checkingsaccount import CheckingAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.data_file = "database_bank.json"
        self.load_data()

    def create_account(self, account_type,account_number, owner_name, pin, initial_balance=0, **kwargs):
        if account_number in self.accounts:
            return (False, f"Account number {account_number} already exists.")
        
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, owner_name, pin, initial_balance, **kwargs)
        elif account_type.lower() == "checking":
            account = CheckingAccount(account_number, owner_name, pin, initial_balance, **kwargs)
        else:
            return (False, "Invalid account type. Must be 'savings' or 'checking'.")
        
        self.accounts[account_number] = account
        self.save_data()
        return (True, f"{account_type.title()} account created for {owner_name} with account number {account_number}.")
        

    

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, from_account_number, to_account_number, amount, pin):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if not from_account:
            return (False, f"From account number {from_account_number} does not exist.")
        if not to_account:
            return (False, f"To account number {to_account_number} does not exist.")
        
        success, message = from_account.withdraw(amount, pin)
        if not success:
            return (False, message)
        
        to_account.deposit(amount)
        self.save_data()
        return (True, f"Transferred ${amount:.2f} from account {from_account_number} to account {to_account_number}.")

    def save_data(self):
        data = {}
        for account_number, account in self.accounts.items():
            data[account_number] = {
                "account_type": "savings" if isinstance(account, SavingsAccount) else "checking",
                "owner_name": account.owner_name,
                "pin": account.pin,
                "balance": account.balance,
                "transaction_history": [
                    {
                        "transaction_type": t.transaction_type,
                        "amount": t.amount,
                        "timestamp": t.timestamp
                    } for t in account.transaction_history
                ]
            }
            if isinstance(account, SavingsAccount):
                data[account_number]["interest_rate"] = account.interest_rate
                data[account_number]["min_balance"] = account.min_balance
            elif isinstance(account, CheckingAccount):
                data[account_number]["overdraft_limit"] = account.overdraft_limit

        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return
        
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        
        for account_number, account_data in data.items():
            if account_data["account_type"] == "savings":
                account = SavingsAccount(
                    account_number,
                    account_data["owner_name"], 
                    account_data["pin"], 
                    account_data["balance"],
                    interest_rate=account_data.get("interest_rate", 0.01),
                    min_balance=account_data.get("min_balance", 100)
                )

            else:  # checking account
                account = CheckingAccount(
                    account_number,
                    account_data["owner_name"], 
                    account_data["pin"], 
                    account_data["balance"],
                    overdraft_limit=account_data.get("overdraft_limit", 100)
                )

            if "transaction_history" in account_data:
                from transaction import Transaction
                for t_data in account_data["transaction_history"]:
                    transaction = Transaction(
                        t_data["transaction_type"],
                        t_data["amount"],
                        account
                    )
                    transaction.timestamp = t_data["timestamp"]
                    account.transaction_history.append(transaction)

            self.accounts[account_number] = account