class Employee:
    pass
    
    def __init__(self,a,b,c):
        self.name=a
        self.emp_id=b
        self.salary=c
    

def main():
    obj=Employee("Rohit",101,5000)
    print("Name :",obj.name)
    print("ID :",obj.emp_id)
    print("Salary :",obj.salary)
if __name__=="__main__":
    main()