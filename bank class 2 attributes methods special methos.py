class Account:
    owner=''
    balance=0

    def __init__(self,name,balance):
        self.owner=name
        self.balance=balance

    def deposit(self,depo):
        self.balance=self.balance+depo
        print('Deposit Accepted')

    def withdraw(self,loan):
        if(self.balance>loan):
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')
    def __str__(self):
        return f"Account Owner:{self.owner}\nAccount Balance:{self.balance}"
acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)

