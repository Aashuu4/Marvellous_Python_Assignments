class BookStore:
    NoOfBooks=0
    def __init__(self,a,b):
        self.name=a
        self.author=b
        BookStore.NoOfBooks+=1
    def Display(self):
        print("Name of Book :",self.name)    
        print("Author of Book :",self.author)  
        print("Number of Books :",BookStore.NoOfBooks)
    
    

def main():
    obj1=BookStore("linux system programming","Robert love")
    obj1.Display()
    
    obj1=BookStore("C programming","Dennis Ritchie")
    obj1.Display()

if __name__=="__main__":
    main() 