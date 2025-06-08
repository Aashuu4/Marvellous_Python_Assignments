
def sum(n1,n2):
    return n1+n2
def difference(n1,n2):
    return n1-n2
def product(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2



def main():
    print("Enter the first number")
    n1=int(input())
    print("Enter the second number")
    n2=int(input())
    
    s= sum(n1,n2)
    diff=difference(n1,n2)
    p=product(n1,n2)
    d=division(n1,n2)
    
    print("sum of :",n1 ,"&",n2 ,"=",s)
    print("difference of :",n1 ,"&",n2 ,"=",diff)
    print("product of :",n1 ,"&",n2 ,"=",p)
    print("division of :",n1 ,"&",n2 ,"=",d)
       
    

if __name__=="__main__":
    main()