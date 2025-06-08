class BankAccount:
    
    def __init__(self,a,b,c):
        self.account_number=a
        self.name=b
        self.balance=c
        
    def deposit(self):
        print("Enter the amount to deposit")
        deposit=float(input())
        self.balance+=deposit
        print("balance after deposit :",self.balance)
        
    def withdraw(self):
        print("Enter the amount to withdraw")
        withdraw=float(input())
        self.balance-=withdraw
        print("balance after deposit :",self.balance)
        
    def Display(self):
        print("Balance :",self.balance)
        
        
def main():
    obj1=BankAccount(6710609899,"Rahul",5000)
    obj1.deposit()
    obj1.withdraw()
    obj1.Display()
    
if __name__=="__main__":
    main()