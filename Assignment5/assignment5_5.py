
def oddeven(n1):
    if(n1%2==0):
        print(n1,": is a even number")
    else:
        print(n1,": is a odd number")
def main():
    print("Enter the number to check")
    n1=int(input())
    oddeven(n1)

if __name__=="__main__":
    main()