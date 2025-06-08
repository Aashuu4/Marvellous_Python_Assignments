

def fdata(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
     return num  
 
   
def main():
    print("Enter the size of list")
    n1=int(input())
    number=[]
    for i in range(n1):
        print("Enter the number to add")
        num=int(input())
        number.append(num)
        
    data=(list(filter(fdata,number)))
    print("Prime number  :",data) 


if __name__=="__main__":
    main()