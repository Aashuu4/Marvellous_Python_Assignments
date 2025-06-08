
def area(l,w):
    Area = l * w
    print("Area of rectangle is :",Area)

def perimeter(l,w):
    Perimeter = 2 * (l + w)
    print("Perimeter of rectangle is :",Perimeter)

def main():
    print("enter the length")
    l=int(input())
    print("enter the width")
    w=int(input())
    
  
    area(l,w)
    
    perimeter(l,w)
            

if __name__=="__main__":
    main()