## list of the randomly generated passwords

from random import randint

def main() :
    for j in range(10):
        for i in range(4) :
            a= str(randomCharacter("bcdfghjk1mnpqrstvwxz"))
            b= str(randomCharacter("aei0uy"))
            print(a+b,end='')
        print()
        
    
def randomCharacter(characters) :
    n = len(characters)
    r = randint(0, n - 1)
    return characters[r]

main()

## stop
from os import system
system("pause")