def primenumb(n1):
    count=0
    for i in range(1,n1+1):
        if(n1%i==0):
            count=count+1
            
    if(count==2):
        print(n1,": is Prime number")
    else:
        print(n1,":is not Prime number")


def main():
     print("Enter the number ")
     n1 =int(input())
     primenumb(n1)


if __name__=="__main__":
    main()