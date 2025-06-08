from functools import reduce

def even(num):
    return (num%2==0)

def square(num):
    return num*num

def sum(a,b):
    return a+b

def main():
    
    print("enter of elemnts to add")
    n1=int(input())
    number=[]
    for i in range(n1):
        print("enter the number to add in list")
        n2=int(input())
        number.append(n2)
        # print(number)
        
     
    fdata=(list(filter(even,number)))
    print("Filter data :",fdata)
        
    mdata=(list(map(square,fdata)))
    print("Map data :",mdata)
    
    rdata=(reduce(sum,mdata))
    print("Reduce data",rdata)


if __name__=="__main__":
    main()