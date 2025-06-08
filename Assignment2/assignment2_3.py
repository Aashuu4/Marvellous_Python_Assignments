
def factorial(n1):
 fact =1
 while(n1>=1):
    fact=fact*n1
    n1=n1-1
    
 return fact

def main():
    
    print("enter the number ")
    n1=int(input())
    
    result=factorial(n1)
    print(result)

if __name__=="__main__":
    main()
    
    
    
