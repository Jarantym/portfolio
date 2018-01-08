## FASTA-imitating files generator


from random import randint


def main():
	print()
	print('FOR GENERATING FILE, PLEASE,')
	print()
	## name of file
	inpName=input("Enter the name of the future protein: ")	
	
	## create file
	output_1=open(inpName + ".fasta", "w")
	
	## create header in the file
	output_1.write('>' + inpName + '\n')
	
	## the sequence generating
	for i in range(1000):
		a = str(pepCreate("ACGT"))
		
		
		## sequence file inscripting
		output_1.write(a)
	print()
	output_1.write('\n')
	print("Sequence in the file " + inpName + ".fasta" + " successfully created!")
	print("To open file, please, input " + "'cat " + inpName + ".fasta'" + " to command line")
	print()

## the generating function
def pepCreate(characters):
	n = len(characters)
	r = randint(0, n - 1)
	return characters[r]



main()

## stop
from os import system
system("pause")
