def countnumb(n1):
    count=0
    
    while(n1>0):
        rem=n1%10
        count=count+1
        n1=n1//10
    print(count)

def main():
     print("Enter the number ")
     n1 =int(input())
     countnumb(n1)


if __name__=="__main__":
    main()