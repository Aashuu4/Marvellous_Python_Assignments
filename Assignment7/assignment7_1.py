square=lambda a :a*a
cube=lambda a :a**a
def main():
    print("enter the number")
    num=int(input())
    ret=square(num)
    print("Square of number is :",ret)
    ret=cube(num)
    print("Cube of number is :",ret)


if __name__=="__main__":
    main()