class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.balance=balance
        self.int_rate=int_rate
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    #     # your code here
    def withdraw(self, amount):
        self.balance -= amount
        return self
    #     # your code here
    def display_account_info(self):
        print(self.balance)
        print(self.int_rate)
        return self
    #     # your code here
    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        # your code here

accountone = BankAccount(5,100)
accounttwo = BankAccount(2, 50)

accountone.display_account_info().deposit(10).deposit(10).deposit(10).withdraw(25).display_account_info()
accounttwo.display_account_info().deposit(10).deposit(10).withdraw(5).withdraw(10).withdraw(10).withdraw(5)

print(accountone.balance)
print(accounttwo.balance)
