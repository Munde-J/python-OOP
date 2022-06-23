from datetime import datetime

class Account:

    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.transaction_cost = 100
        self.full = []
        self.datetime = datetime.now().strftime("%x %X")
        self.loan_balance = 0

    def deposit(self,amount):
        if amount <=0:
            return f"Deposit must be greater than zero"

        else:
            self.balance += amount
            now = datetime.now()
            statement = {"date":now,"amount":amount,"narration":f"Hello {self.name} you have deposited {amount}, your new balance is {self.balance}"}
            self.deposits.append(statement)
            print(self.deposits)

#conditions for the withdrawal to be successful, requested amount must be
# greater than current balance, and must be greater than zero. 
       
    def withdraw(self,amount):
        if amount>self.balance:
            return f"Insufficient funds"

        elif amount<=0:
            return f"Amount must be greater than zero"

        if amount+self.transaction_cost>self.balance:
            return f"Insufficient balance"

        else: 
            now=datetime.now()
            statement = {"date":now,"amount":amount,"narration":f"Hello {self.name} you have withdrawn {amount}, your new balance is {self.balance}"}
            self.balance -= amount + 100
            self.withdrawals.append(statement) 
            print(self.withdrawals)          
        
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

# #Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

# Update the deposit method to store each deposit transaction as a dictionary like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

# Add a new method  full_statement which combines both deposits and withdrawals into one list ordered by date and using a for loop prints each transaction in a new line like this
# 16/06/22 —----- Deposit —---- 1000

    def full_statement(self):
        for statement in self.full:
            self.datetime = statement["date"]
            amount = statement["amount"]
            narration = statement["narration"] 
            print(f"{self.datetime} _____{amount}_____{narration}")    

# Add a new attribute loan_balance which is zero by default.
# Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
# Customer account has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.

# Add a loan repayment method with these conditions
# A customer can repay a loan to reduce the current loan balance
# Overpayment of a loan increases a customers current deposit

# Add a new method transfer which accepts two attributes (amount and instance of another account).
# If the amount is less than the current instances balance, the method transfers the requested amount from the current account to the passed account. 
# The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account.

    def borrow(self, amount):
        number_of_deposits = len(self.deposits)
        deposits_sum = 0
        for n in self.deposits:
            deposits_sum+=n['amount']
        
        limit = deposits_sum*(1/3)

        if amount<=100:
            return "your loan must be more than 100 "
        elif self.loan_balance>0:
            return f"Dear customer you still have a loan of {self.loan_balance}"
        elif self.balance!=0:
            return f"You have money in your account"

        elif number_of_deposits<10:
            return f"Your deposits must be atleast 10"
        elif amount>limit:
            return f"Dear customer you can't borrow {amount} it is higher than the limit of {self.balance}"
        else:
            interest=amount*(3/100)
            self.loan_balance+=amount+interest
            return f"Dear customer {self.name} your loan of ksh{amount} has been granted successfully"
            
    def loan_repay(self,amount):
        if amount<=self.loan_balance:
            self.loan_balance-=amount
            return f"Dear customer you have paid {amount} and your loan balance is {self.loan_balance}"
        else:
            over_pay = amount-self.loan_balance
            self.loan_balance=0
            self.balance+=over_pay
            return f"You succesfully completed paying your loan and the over pay is {over_pay} and your new balance is {self.balance}"

    def transfer(self,amount,account):
        fee= amount*0.05
        Total_amount=fee+amount

        if amount<0:
            return f"Dear customer {self.name} your amount is too low"
        elif Total_amount>self.balance:
            return f"Dear customer {self.name} you balance is {self.balance} and you need atleast {Total_amount}"
        else:
            self.balance-=Total_amount
            account.balance+=amount
            return f"Dear customer you  have sent {amount} to {account} and your new balance is {self.balance}"



   



    
       
        
        
        




     




