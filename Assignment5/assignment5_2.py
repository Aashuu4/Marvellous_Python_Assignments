

def check(c):
    if(c=='a'or c=='e'or c=='i'or c=='o'or c=='u'or c=='A'or c=='E'or c=='I'or c=='O'or c=='U' ):
        print("Char ",c,"is a vowel")
    else:
        print("Char ",c,"is a consonant")    

def main():
    print("Enter the char to check")
    char =str(input())
    
    check(char)

if __name__=="__main__":
    main()