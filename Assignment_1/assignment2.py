def chksum(value):
    
    if(value%2==0):
     print(value,"Is Even Number")
    else:
       print(value,"Is Odd Number")
      
    

def main():
    print("Enter the number to check")
    no1=int(input())

    chksum(no1)

if __name__=="__main__":
    main()