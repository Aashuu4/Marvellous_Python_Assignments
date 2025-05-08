def check(n1):
    if(n1>0):
        print(n1," is Positive Number")
    if(n1==0):
        print(n1,"is Zero")
    if(n1<0):
        print(n1,"is Negative Number")
    


def main():
    print("Enter the number to check whether it is positive or negative and Zero")
    
    number = int(input())
    check(number)
    

if __name__=="__main__":
    main()