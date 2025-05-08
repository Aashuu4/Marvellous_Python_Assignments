def Add(n1,n2):
    result=n1+n2
    return result
    
    
def main():
    print("Enter the First Number")
    number1 =int(input())
    print("Enter the Second Number")
    number2 =int(input())
    
    calculate =Add(number1,number2)
    print("Addition of both the number is :" ,calculate)


if __name__=="__main__":
   main()