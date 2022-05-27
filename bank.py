
# class Account:
#     accountname ="Angela"
#     accountnumber = 234564
#     password = 545454
#     bank_name="kcb"

# class Account:
#     bank_name="kcb"
#     def __init__(self,accountname,accountnumber,password):
#         self.accountname=accountname
#         self.accountnumber=accountnumber
#         self.password=password

#Add these methods to class Account - deposit, withdraw.
#Create two instances of account and verify they work as expected.


class Account:

    def __init__(self,account_name,account_number,balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        return f"Hello {self.account_name} of account number {self.account_number}, your new balance {self.balance}"
        
    def withdraw(self,amount):
        self.balance-=amount
        return f"Hello {self.account_name} of account number {self.account_number}, your new balance is  {self.balance}"
             
        



    
       
        
        
        




     




