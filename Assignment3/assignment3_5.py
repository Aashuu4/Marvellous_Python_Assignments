import marvellousnum

def main():
    print("enther the number of elements")
    n1=int(input())
    number=[]
    ListPrime=[]
    for n1 in range(n1):
        print("enter the values ")
        num=int(input())
        number.append(num)
    print(number)
    for num in number:
        if (marvellousnum.chkprime(num)):
            ListPrime.append(num)
    print(ListPrime)       
        
if __name__=="__main__":
    main()
    
    
    
    
    
    
    
