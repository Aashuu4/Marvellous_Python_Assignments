from functools import reduce

def greater(num):
    return (num>=70 and num<=90)

def increase(num):
    return num+10

def product(a,b):
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
        
     
    fdata=(list(filter(greater,number)))
    print("Filter data :",fdata)
        
    mdata=(list(map(increase,fdata)))
    print("Map data :",mdata)
    
    rdata=(reduce(product,mdata))
    print("Reduce data",rdata)


if __name__=="__main__":
    main()