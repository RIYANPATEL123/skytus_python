class BankAccount:
    def __init__(self,accname,balance):
        self.accname = accname
        self.balance = balance
    
    def deposit(self,deposit):
        self.balance += deposit
    
    def withdraw(self,withdraw):
        self.balance -=  withdraw
    
b = BankAccount("riyan",10000)
print(f"The acc name {b.accname}")
print(f"The balance is {b.balance}")

b.deposit(3000)
print(f"Balance after depositing money {b.balance}")

b.withdraw(2000)
print(f"Balance after withdrawing money {b.balance}")