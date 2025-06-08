from functools import reduce


def add(a,b):
    return a+b

def main():
     print("Enter the number of elements ")
     n=int(input())
     number=[]
     for i in range(n):
         num=int(input("enter the value"))
         number.append(num)     
     num1=reduce(add,number)
     print(num1)
     
     
     
   


if __name__=="__main__":
    main()