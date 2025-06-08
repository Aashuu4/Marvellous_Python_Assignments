
def printnumber(n1):
    for i in range(1,n1+1):
        print(i)


def main():
    print("enter the end number")
    n1=int(input())
    printnumber(n1)

if __name__=="__main__":
    main()