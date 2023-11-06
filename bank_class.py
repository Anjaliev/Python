class bank:
    def __init__(self,acc_num,name,type,balance):
        self.acc_num=acc_num
        self.name=name
        self.type=type
        self.balance=balance
    def deposit(self,amnt1):
        self.balance+=amnt1
        print("Current balance =",self.balance)
    def withdraw(self,amnt):
        if amnt>self.balance:
            print("Invalid")
        else:
            self.balance-=amnt
            print("After withdraw Balance=",self.balance)
    def display(self):
        print("Account number =",self.acc_num)
        print("Customer name =",self.name)
        print("Account type =",type)
        print("Account balance =",self.balance)
acc_num=int(input("Enter the account number:"))
name=input("Enter the name:")
type=input("Enter the type:")
balance=int(input("Enter the balance:"))
b=bank(acc_num,name,type,balance)
amnt1=int(input("Enter the deposit amount:"))
b.deposit(amnt1)
amnt=int(input("Enter the withdrawal amount:"))
b.withdraw(amnt)
b.display()
