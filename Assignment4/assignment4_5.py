from functools import reduce

def prime(num):
    
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
    
     return num

def multiply(num):
    return num*2

def max1(a,b):
    return a if a > b else b
    
            
            
    
   

def main():
    
    print("enter of elemnts to add")
    n1=int(input())
    number=[]
    for i in range(n1):
        print("enter the number to add in list")
        n2=int(input())
        number.append(n2)
        # print(number)
        
     
    fdata=(list(filter(prime,number)))
    print("Filter data :",fdata)
        
    mdata=(list(map(multiply,fdata)))
    print("Map data :",mdata)
    
    rdata=(reduce(max1,mdata))
    print("Reduce data",rdata)


if __name__=="__main__":
    main()