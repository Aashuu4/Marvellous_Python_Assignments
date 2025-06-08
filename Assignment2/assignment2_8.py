def main():

 print("Enter the number ")
 n1 =int(input())
 
 for i in range(1,n1+1):
     for j in range(1,i+1):
       print(j, end=" ")
     print()
   

if __name__=="__main__":
    main()