## simple numbs

## BEST VARIANT!!!



def main():
	
	c=simpNums(100)
	print(c)
	
## functiom creating list of simple numbers in a list	
def simpNums(scope):
	
	c= []
	for i in range(2,scope):
		c.append(i)
	for i in range(2,int(scope/10)):
		for j in c:
			if j%i==0 and not j==i:
				c.remove(j)
	return c



main()

## stop
from os import system
system("pause")
