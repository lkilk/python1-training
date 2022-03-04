#from abc import ABC, abstractmethod

class Account:
    def __init__(self, name, balance=0):
        self.__name = name
        self.__balance = balance 
        self.interest_rate = 0.1

    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self, name):
        if name != None and len(name) > 0:
            self.__name = name
        else:
            print("Invalid input")

    @property
    def balance(self): 
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount #self.balance = self.balance + amount

    # @abstractmethod
    # def withdrawl(self):
        # ...

    def apply_interest(self, rate=1):
        interest = self.__balance * self.interest_rate
        self.__balance += interest

    def __str__(self):
        return f"Account details\t name: {self.name} \t balance: {self.__balance}"

# acc1 = Account("James Brown", 100) 
# #print(acc1)

# #acc1.apply_interest()
# #print(acc1)
# print(acc1.name)
# acc1.name = "Marvin Gaye"
# print(acc1.name)

# print(acc1)

