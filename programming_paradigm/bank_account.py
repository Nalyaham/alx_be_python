class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        result = amount + self.account_balance

    def withdraw(self, amount):
        if amount >= self.account_balance:
            result = self.account_balance - amount

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
