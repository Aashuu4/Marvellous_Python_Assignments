
def main():
    print("Enter the number for which you want to print the table ")
    num=int(input())
    for i in range(1,11):
        print(num,"*",i,"=",num*i)


if __name__=="__main__":
    main()