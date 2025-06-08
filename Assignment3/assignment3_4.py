def main():
    
     print("Enter the number of elements ")
     n=int(input())
     number=[]
     for i in range(n):
         num=int(input("enter the value"))
         number.append(num) 
     print(number)
     count=0
     print("Enter the number you want to check frequency")
     check=int(input())
     for num in number:
        if check==num:
            count+=1
     print(count)       


if __name__=="__main__":
    main()
    