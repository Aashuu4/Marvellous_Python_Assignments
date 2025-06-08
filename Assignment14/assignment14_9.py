class Product:
    
   
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if( self.price == other.price):
            print("Price of both the products is same")
        else:
            print("Price of both the products is not  same")
            
        

def main():
    obj1 = Product("Apple", 10)
    obj2 = Product("Orange", 12)
    Product.__eq__(obj1,obj2)
    
if __name__=="__main__":
    main()


