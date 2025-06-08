
from functools import reduce
def rdata(a,b):
    return a+b
def main():
    print("Enter the size of list")
    n1=int(input())
    number=[]
    for i in range(n1):
        print("Enter the number to add")
        num=int(input())
        number.append(num)
        
    data=(reduce(rdata,number))
    print("Product  :",data) 


if __name__=="__main__":
    main()