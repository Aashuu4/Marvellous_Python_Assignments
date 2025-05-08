def check(n1):
    if(n1%5==0):
        print(True)
    else:
        print(False)    
    

def main():
    print("Enter the number ")
    n1=int(input())
    
    check(n1)

if __name__=="__main__":
    main()