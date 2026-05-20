class SavingsAccount:
    def __init__(self, balance):
        self.balance = balance

class CurrentAccount:
    def __init__(self, balance):
        self.balance = balance


savings = SavingsAccount(5000)
current = CurrentAccount(3000)
print(f"Savings balance: {savings.balance}")
print(f"Current balance: {current.balance}")
