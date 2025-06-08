def fahrenheit(c):
    f=(c * 9/5) +32
    print("temperature in fahrenheit :",f,"f")
    
def main():
    print("enter the temperature to convert in celsius")
    n1=int(input())
    fahrenheit(n1)

if __name__=="__main__":
    main()