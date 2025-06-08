class Numbers:
    
    def __init__(self,a):
        self.value=a
    def chkprime(self):
        if(self.value%2==0):
            return True
        else:
            return False
    def chkperfect(self):
        sum=0
        for i in range(1,self.value):
            if(self.value%i==0):
                sum+=i
        if(sum==self.value):
         return True
        else:
         return False    
        
    def sumfactor(self):
        sum=0
        for i in range(1,self.value+1):
            if(self.value%i==0):
                sum+=i         
        print("Addition of all the factors is :",sum)
                
        
    def factors(self):
        
        for i in range(1,self.value+1):
            if(self.value%i==0):
             print(i)

        

def main():
    obj1=Numbers(6)
    print(obj1.chkprime())
    
    print(obj1.chkperfect())
    obj1.factors()
    obj1.sumfactor()


if __name__=="__main__":
    main()