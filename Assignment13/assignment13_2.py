class BankAccount:
    ROI=10.5
    def __init__(self,a,b):
        self.name=a
        self.amount=b
    def Display(self):
        print("Account holder name :",self.name)
        print("Amount:",self.amount)
    def Deposit(self):
        print("Enter the amount you want to deposit")
        amount=float(input())
        self.amount+=amount
    def Withdraw(self):
        print("enter the amount you want to withdraw")
        withdraw=float(input())
        self.amount-=withdraw
    def CalculateIntrest(self):
        interest=self.amount*BankAccount.ROI/100
        print("Rate of interset:",interest)
        
      
def main():
    obj1=BankAccount("Ashutosh",5000)
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateIntrest()
    obj1.Display()

if __name__=="__main__":
    main()