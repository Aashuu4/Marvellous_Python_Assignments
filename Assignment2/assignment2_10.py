def countnumb(n1):
    sum=0
    
    while(n1>0):
        rem=n1%10   #123%10=3
        sum=sum+rem
        n1=n1//10
    print(sum)

def main():
     print("Enter the number ")
     n1 =int(input())
     countnumb(n1)


if __name__=="__main__":
    main()