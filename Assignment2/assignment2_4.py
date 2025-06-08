def factadd(n1):
    sum=0
    for i in range(1,n1+1):
        if(n1==i):
            break
        if(n1%i==0):
             sum+=i 
    return sum

           
    
def main():
    print("Enter the number ")
    n1 =int(input())
    result= factadd(n1)
    print("Addition of factors of ",n1,"is : ",result)

if __name__=="__main__":
    main()
    
    

     
    
    
    
    
