from account_class import Account
from savings_account import SavingsAccount

class CreditAccount(Account): 

    def __init__(self, name, credit_limit, balance=0):
        super().__init__(name, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if (self.balance - amount) > (self.balance - self.credit_limit): 
            self.balance -= amount
        else:
            print(f"withdrawl exceeds credit limit")

    def apply_interest(self):
        if self.balance >= 0 :
            self.balance *= (1 + self.interest_rate) 
        else:
            self.balance *= (1 - self.interest_rate)

class Bank: 

    def __init__(self, name):
        self.name = name
        self.accounts = dict()

    def add_account(self, acc, id):
        self.accounts[id] = acc

bank = Bank('Lloyds')                                            
#bank.add_account(Account('Liam', 1000), 111)     
bank.add_account(CreditAccount('George', 500, 1000), 112)
bank.add_account(SavingsAccount('Sarah', 1000), 113)

for acc in bank.accounts.values():
    print(acc)