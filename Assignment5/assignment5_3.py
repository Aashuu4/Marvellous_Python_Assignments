
def voting(age):
    if(age>=18):
        print("Eligible to Vote")
        
    else:
        print("Not Eligible To Vote")    
        
def main():
    print("Enter your age ")
    age=int(input())
    voting(age)


if __name__=="__main__":
    main()