# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:54:46 2023
Adapted (Iain Martin) from the Example from Learning Scientific Programmign 
with Python, C.Hill, 4.6.2
@author: 
"""


class BankAccount:
    
    currency = "£"
    def __init__(self, customer, account_number, balance=0):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
        
        
    def deposit(self, amount)->None:
        if (amount > 0):
            self.balance += amount
        else:
            print ("Invalid amount")
            
    def withdraw(self, amount)->None:
         if (amount <= self.balance):
            self.balance -= amount
         else:
            print ("Sorry, not enough funds!")
            
    def check_balance(self)->None:
         print ("Balance of a/c {:d} is {:s}{:.2f}".format(self.account_number, self.currency, self.balance))
        
     
class SavingsAccount(BankAccount):
    def __init__(self, customer, account_number, interest_rate, balance=0):
        self.interest_rate = interest_rate
        super().__init__(customer, account_number,balance)
        
    def add_interest(self)->None:
        interest = self.balance*self.interest_rate/100;
        self.balance += interest
        
# Test our BankAccount    
myAccount = BankAccount (1, 123456, 100)
myAccount.check_balance()
myAccount.withdraw(20)
myAccount.check_balance()
myAccount.deposit(10)
myAccount.check_balance()
print()


# Test our SavingsAccount  
mySavingsAccount = SavingsAccount(1, 123456, 5.0, 100)
mySavingsAccount.check_balance()
mySavingsAccount.withdraw(20)
mySavingsAccount.check_balance()
mySavingsAccount.deposit(10)
mySavingsAccount.add_interest()
mySavingsAccount.check_balance()

