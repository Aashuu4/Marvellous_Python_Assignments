class Calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
        
    def add(self):
        add=self.num1+self.num2
        print("Addition of Numbers is :",add)
        
    def sub(self):
        sub=self.num1-self.num2
        print("Subtraction of Numbers is :",sub)
        
    def div(self):
        div=self.num1/self.num2
        print("Division of Numbers is :",div)
        
    def mult(self):
        mult=self.num1*self.num2
        print("Multiplication of Numbers is :",mult)
        
        
def main():
    obj1=Calculator(10,5)
    obj1.add()
    obj1.sub()
    obj1.div()
    obj1.mult()
    
    
if __name__=="__main__":
    main()