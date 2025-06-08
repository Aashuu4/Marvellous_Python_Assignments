def main():
    sum=0
    for i in range(1,100+1):
        if(i%2==0):
            sum+=i
    print("Sum of Even numbers between 1 to 100 is :",sum)
            

if __name__=="__main__":
    main()