def fdata(num):
    return num%2==0
def main():
    print("Enter the size of list")
    n1=int(input())
    number=[]
    for i in range(n1):
        print("Enter the number to add")
        num=int(input())
        number.append(num)
        
    data=list(filter(fdata,number))
    print("Even number :",data)    


if __name__=="__main__":
    main()