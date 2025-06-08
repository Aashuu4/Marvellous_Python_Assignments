def main():
    
     print("Enter the number of elements ")
     n=int(input())
     number=[]
     for i in range(n):
         num=int(input("enter the value"))
         number.append(num) 
     print(number)
     max=number[0]
     for i in number:
      
      if i>max:
          max=i
     print(max)      


if __name__=="__main__":
    main()
    