import arithmetic


def main():
    
    print("Enter the first number")
    n1=int(input())
    print("Enter the second  number")
    n2=int(input())
    
    print("Enter which task you want to perform addition subtraction multiplication division")
    
    str =input()
    if(str==("addition")):
        addition=arithmetic.add(n1,n2)
        print("Addition of both the number is :",addition)
    
    elif(str==("subtraction")):
        subtraction=arithmetic.sub(n1,n2)
        print("Subtraction of both the number is :",subtraction)
        
    elif(str==("multiplication")):
        multiplication=arithmetic.mult(n1,n2)
        print("Multiplication of both the number is :",multiplication)
        
       
    elif(str==("division")):
        division=arithmetic.div(n1,n2)
        print("Division of both the number is :",division)  
        
        
    else:
        print("Invalid operation. Please enter a valid option.")      
        



if __name__=="__main__":
    main()