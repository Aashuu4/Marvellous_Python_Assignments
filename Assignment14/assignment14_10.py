class Employee:
    def __init__(self,a,b,c):
        self.__salary=a
        self._department=b
        self.name=c
        
    def get_salary(self):
           return self.__salary
        
        
        
def main():
    obj1=Employee(50000,"computer","Rahul")
    obj2=Employee(60000,"E&TC","Rohit")
    obj3=Employee(70000,"Electrical","Ramesh")
    
    print("Name of Employee :",obj1.name)
    print("Salary of Employee :",obj1.get_salary())
    print("Department of Employee :",obj1._department)
    
    print("Name of Employee :",obj2.name)
    print("Salary of Employee :",obj2.get_salary())
    print("Department of Employee :",obj2._department)
    
    print("Name of Employee :",obj3.name)
    print("Salary of Employee :",obj3.get_salary())
    print("Department of Employee :",obj3._department)
    
if __name__=="__main__":
    main()
        