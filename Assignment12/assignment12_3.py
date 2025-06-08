class Arithmetic:
    pass
    def __init__(self):
     self.value1=0
     self.value2=0
    
    def accept(self):
        print("enter the first number")
        self.value1=int(input())
        print("enter the second number")
        self.value2=int(input())
    
    def Addition(self):
        add=self.value1+self.value2
        return add
    def subtraction(self):
        sub=self.value1-self.value2
        return sub
    def multiplication(self):
        mult=self.value1*self.value2
        return mult
    def division(self):
        div=self.value1/self.value2
        return div
    
def main():
    obj1=Arithmetic()
    obj1.accept()
    print ("Addition :",obj1.Addition())
    print("Subtraction :",obj1.subtraction())
    print("Multiplication :",obj1.multiplication())
    print("Division :",obj1.division())
if __name__=="__main__":
    main()   