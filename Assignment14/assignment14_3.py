class Book:
    def __init__(self,a):
     self.__value=a
     
    def set_value(self,value1):
         self.__value =value1
    
    def get_value(self):
        return self.__value
    
def main():
    obj1=Book(5)
    obj1.set_value(10)
    # obj1.get_value()
    print(obj1.get_value())
if __name__=="__main__":
    main()