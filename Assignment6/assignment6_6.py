def main():
    row=1
    print("Enter the number ")
    n1 =int(input())
    for i in range(n1+1):
        for j in range(i+1):
            row=row+1
        print("*"*j)
        
        #   print()
if __name__=="__main__":
    main()