class Vehicle:
    def start(self):
        print("vehicle is started")
    
class car(Vehicle):
    def start(self):
         print("car is started")
         
         
def main():
    v=Vehicle()
    v.start()
    c=car()
    c.start()
    
    
if __name__=="__main__":
    main()