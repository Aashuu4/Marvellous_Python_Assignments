class Rectangle:
    def __init__(self,a,b):
        self.length=a
        self.width=b
        
    def area(self):
        area=self.length*self.width
        print("Area of rectangle:",area)
        
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        print("Perimeter of rectangle:",perimeter)
        
def main():
    obj1=Rectangle(5,10)
    obj1.area()
    obj1.perimeter()
    
if __name__=="__main__":
    main()