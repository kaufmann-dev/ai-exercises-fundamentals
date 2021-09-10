#!/usr/bin/env python
# coding: utf-8

# In[21]:


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_frozen = False
        print("Welcome to your new bank account.")
    def freezeAccount(self):
        if self.is_frozen:
            print("Account is already frozen. Contact bank.")
        else:
            self.is_frozen = True
            print("Successfully froze account. Contact bank.")
    def checkBalance(self):
        if self.is_frozen:
            print("Cant withdraw from a frozen account")
        else:
            print(f"Your current balance is {self.balance} euros.")
    def withdraw(self, amount):
        if self.is_frozen:
            print("Cant withdraw from a frozen account.")
        else:
            if (self.balance - amount) >= -1000:
                self.balance = self.balance - amount
                print(f"Successfully withdrew {amount} euros.")
            else:
                print(f"You do not have enough balance to withdraw {amount} euros.")
    def deposit(self, amount):
        if self.is_frozen:
            print("Can't deposit to a frozen account.")
        else:
            self.balance = self.balance + amount
            print(f"Successfully deposited {amount} euros.")


# In[22]:


bank = BankAccount()
bank.deposit(1000)
bank.checkBalance()
bank.withdraw(2000)
bank.checkBalance()


# In[ ]:




