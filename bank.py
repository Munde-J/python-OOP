             
class Account:

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []

    def deposit(self,amount):
        if amount <=0:
            return f"Deposit must be greater than zero"

        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f"Hello {self.name} you have deposited {amount}, your new balance {self.balance}"

#conditions for the withdrawal to be successful, requested amount must be
# greater than current balance, and must be greater than zero. 
       
    def withdraw(self,amount):
        if amount>self.balance:
            return f"Insufficient funds"

        elif amount<=0:
            return f"Amount must be greater than zero"

        else:    
         self.balance -= amount + 100
         self.balance = self.withdrawals.append(amount) 
         return f"Hello {self.name} you have withdrawn {amount}, your new balance {self.balance}"             
        
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.
    
    def deposits_statement(self):
        for x in self.deposits:
            print (f"Your deposit is {x}","/n" )

    def withdrawals_statement(self):
        for x in self.withdrawals:
            print (f"Your withdrawal is {x}", "/n")       



   



    
       
        
        
        




     




