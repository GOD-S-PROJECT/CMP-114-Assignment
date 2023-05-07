class SavingsAccount:
    def _init_(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Insufficient funds for withdrawal.")

    def check_balance(self):
        print(f"Account balance: ${self.balance}")


# Example usage:
account = SavingsAccount(650)  # Creating an account with an initial balance of $650
account.check_balance()  # Output: Account balance: $650

account.deposit(520)  # Deposit $520
account.check_balance()  # Output: Account balance: $1170

account.withdraw(250)  # Withdraw $250
account.check_balance()  # Output: Account balance: $920

account.withdraw(1000)  # Trying to withdraw $1000 (insufficient funds)
account.check_balance()  # Output: Insufficient funds for withdrawal.
