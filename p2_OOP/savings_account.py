from account_class import Account

class SavingsAccount(Account): 

    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def withdraw(self, amount):
        if self.balance < amount: 
            print("Insufficiant funds")
        else:
            self.balance -= amount
            print(f"New balance is £{self.balance}")



# acc = SavingsAccount("liam", 100)
# print(acc)

