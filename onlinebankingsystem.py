import datetime

# Class to represent a Bank Account
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.transaction_history = []  # List to store transaction records

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = self.create_transaction("Deposit", amount)
            self.transaction_history.append(transaction)
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            transaction = self.create_transaction("Withdrawal", amount)
            self.transaction_history.append(transaction)
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    # Method to transfer money to another account
    def transfer(self, recipient_account, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            recipient_account.deposit(amount)
            transaction = self.create_transaction("Transfer", amount, recipient_account.account_number)
            self.transaction_history.append(transaction)
            print(f"Transferred: {amount} to Account {recipient_account.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid transfer amount.")

    # Method to create a transaction record
    def create_transaction(self, transaction_type, amount, recipient_account_number=None):
        transaction = {
            'date': datetime.datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance_after': self.balance,
            'recipient_account': recipient_account_number if recipient_account_number else "N/A"
        }
        return transaction

    # Method to display the transaction history
    def display_transaction_history(self):
        print(f"\nTransaction History for {self.owner_name} (Account: {self.account_number}):")
        for txn in self.transaction_history:
            print(f"{txn['date']} - {txn['type']} of {txn['amount']} | Balance after: {txn['balance_after']} | Recipient: {txn['recipient_account']}")

# Example usage
account1 = BankAccount(account_number="12345", owner_name="John Doe", balance=1000)
account2 = BankAccount(account_number="67890", owner_name="Jane Smith", balance=500)

# Performing some transactions
account1.deposit(500)  # John deposits 500
account1.withdraw(200)  # John withdraws 200
account1.transfer(account2, 300)  # John transfers 300 to Jane

# Displaying transaction histories
account1.display_transaction_history()
account2.display_transaction_history()
