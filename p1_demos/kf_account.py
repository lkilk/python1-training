class Account:
    '''
    This class defines a basic Bank account object. The data properties are number...
    name and balance and the methods are withdraw and deposit.
    When an account object is passed to the print function the output will
    display the number, name and balance.
    '''

    nrOfAccounts = 0 # class variable 
    
    def __init__(self,number,name,balance = 0.0): # This method will execute when an object is created
        self.number = number # object/instance variable is prefixed by self
        self.name = name
        self.__balance = balance # dunder prefix makes this attribute 'private'
        Account.nrOfAccounts += 1

    # def displayDetails(self): # any method to be executed on an object requires self parameter
    #     print(f'Number: {self.number} - Name: {self.name} - Balance: {self.__balance}')

    def __str__(self): 
        return f'Number: {self.number} - Name: {self.name} - Balance: {self.__balance}'

    def withdraw(self, amount ):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print('Insufficient funds')

    def deposit(self, amount ):
        self.__balance += amount

    def setBalance(self,amount): # typically referred to as a setter method
        self.__balance = amount

    def getBalance(self,amount): # typically referred to as a getter method
        return self.__balance

acc1 = Account(1234, 'Stuart' , 1500.00 ) # __init__ executes at this point 
acc2 = Account(2345,'Alan')

# acc1.__balance # We cannot directly access the 'private' attribute by name 
# acc1._Account__balance = 10000 # can access a 'private' attribute using this 'pattern'
acc1.setBalance(2000)
acc2.deposit(3000)

#  acc1.displayDetails()
#  acc2.displayDetails()

print(f'Accounts created: {Account.nrOfAccounts}')

print(acc1)
print(acc1.__doc__)