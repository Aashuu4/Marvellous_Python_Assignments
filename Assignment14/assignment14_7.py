class Person:
    def __init__(self,a,b):
        self.name=a
        self.age=b
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
    
    
    
class Teacher(Person):
    def __init__(self,subject,salary):
        super().__init__
        self.subject=subject
        self.salary=salary
        
    def display(self):
        print("Subject :",self.subject)
        print("salary:",self.salary)  
        
        
def main():
    obj1=Person("Rahul",25)
    obj2=Teacher("maths",25000)
    obj1.display()
    obj2.display()
    
if __name__=="__main__":
    main()