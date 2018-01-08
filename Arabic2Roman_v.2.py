## get arabic cyphers to roman style

print()
print('THIS PROGRAMM WILL HELP YOU TO CHANGE\n ARABIC DIGIT STYLE TO ROMAN ONE')
print()

def main():
    
    
    ## input
    
    p= int(input("enter a number not more 3999: "))
    print('__________________________')
    
    
    ## parts of result
    
    seq=""
    romanMills=''
    romanHunds=''
    romanTens=''
    romanOnes=''
    
    
    ## comparing and filling for result using romanDigit function
    
    if 1<=p<=10:
        romanOnes+=romanDigit(p %10, "I","V","X")
        seq = seq +  romanOnes 
        
    elif 11<=p<=100:
        
        romanOnes+=romanDigit(p %10, "I","V","X")
    
        p=p//10
        romanTens+=romanDigit(p %10, "X","L","C")        
        seq = seq + romanTens + romanOnes 
        
    elif 101<=p<=1000:
        romanOnes+=romanDigit(p %10, "I","V","X")
    
        p=p//10
        romanTens+=romanDigit(p %10, "X","L","C")
    
        p=p//10
        romanHunds+=romanDigit(p %10, "C","D","M")        
        
        seq = seq + romanHunds + romanTens + romanOnes 
        
    elif 1001<=p<=3999:
        romanOnes+=romanDigit(p %10, "I","V","X")
        
        p=p//10
        romanTens+=romanDigit(p %10, "X","L","C")
        
        p=p//10
        romanHunds+=romanDigit(p %10, "C","D","M")
        
        p=p//10
        romanMills+=romanDigit(p %10, "M", "","")
        
        seq = seq + romanMills + romanHunds + romanTens + romanOnes 
        
    else: 
        print('error')
    
    
    ## output   
    
    print(seq)

## function forming roman digits
def romanDigit(n, one, five, ten):
    a=''
    if n==1 or n==2 or n==3:
        a= one*n
    elif n==4:
        a= one+five
    elif n==5 or n==6 or n==7 or n==8:
        a= five+one*(n-5)
    elif n==9:
        a= one+ten    
    else:
        a=''
    
    return a

## start

main()    

## stop
from os import system
system("pause")