def main():
    print("Enter the number")
    num=int(input())
    sum=1
    for i in range(1,num+1):
        sum=sum*i 
    print(sum)    


if __name__=="__main__":
    main()