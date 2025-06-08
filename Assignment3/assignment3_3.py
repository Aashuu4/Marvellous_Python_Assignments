def main():
    
     print("Enter the number of elements ")
     n=int(input())
     number=[]
     for i in range(n):
         num=int(input("enter the value"))
         number.append(num) 
     print(number)
     min=number[0]
     for i in number:
      
      if i<min:
          min=i
     print(min)      


if __name__=="__main__":
    main()
    