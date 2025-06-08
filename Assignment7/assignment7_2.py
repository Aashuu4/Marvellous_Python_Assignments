
def mdata(num):
    return num+num 

def main():
    print("enter of elemnts to add")
    n1=int(input())
    number=[]
    for i in range(n1):
        print("enter the number to add in list")
        n2=int(input())
        number.append(n2)
    
    
    data=list(map(mdata,number))
    print("Doubled List :",data)

if __name__=="__main__":
    main()