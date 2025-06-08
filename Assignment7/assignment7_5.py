
def main():
    print("Enter the name ")
    name=str(input())
    if(name == name[::-1]):    
        print(name+" is a palindrome")
    else:
         print(name +" is not a palindrome")    

if __name__=="__main__":
    
    main()






