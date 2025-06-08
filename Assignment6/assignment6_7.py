def main():
    print("Enter the first number")
    n1=int(input())
    print("Enter the second number")
    n2=int(input())
    print("Enter the third number")
    n3=int(input())
    print("Enter the fourth number")
    n4=int(input())
    print("Enter the fifth number")
    n5=int(input())
    if(n1>n2 and n1>n3 and n1>n4 and n1>n5):
        print("Maximum number is :",n1)
    elif(n2>n1 and n2>n3 and n2>n4 and n2>n5):
        print("Maximum number is :",n2)   
    elif(n3>n1 and n3>n2 and n3>n4 and n3>n5):
        print("Maximum number is :",n3)
    elif(n4>n1 and n4>n2 and n4>n3 and n4>n5):
        print("Maximum number is :",n4)
    elif(n5>n1 and n5>n2 and n5>n3 and n5>n4):
        print("Maximum number is :",n5)
    else:
        print("Invalid")                 
    

if __name__=="__main__":
    main()