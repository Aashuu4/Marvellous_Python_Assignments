    
def main():
    row=5
    print("Enter the number ")
    n1 =int(input())
    for i in range(n1+1):
        print("*"*row)
        row=row-1
        

if __name__=="__main__":
    main()