class Student:
    School_name="zp"
    
    def __init__(self,a,b):
       self.name=a
       self.roll_no=b

def main():
    obj1=Student("rahul",51)
    print("Student name:",obj1.name)
    print("Roll_No of Student:",obj1.roll_no)
    Student.School_name="High School"
    print("School_name:",obj1.School_name)
if __name__=="__main__":
    main()
        