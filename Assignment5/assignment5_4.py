
def largest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print("Largest number is :",n1)
    elif(n2>n1 and n2>n1):
        print("Largest number is :",n2)
    elif(n3>n1 and n3>n1):
        print("Largest number is :",n3)

def main():
    print("Enter the first number")
    n1 =int(input())
    print("Enter the second number")
    n2 =int(input())
    print("Enter the third number")
    n3 =int(input())
    
    largest(n1,n2,n3)

if __name__=="__main__":
    main()