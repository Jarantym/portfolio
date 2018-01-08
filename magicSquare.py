## magic square

# headers and inputs
print()
print('MAGIC SQUARE')
print()
print('enter an odd number:')
n=int(input(''))
print()

# creating matrix
square=[]
for i in range(n):
	datas=[0]*n
	square.append(datas)	

# first position
row=n-1
col=int(n/2)

#first cycle
for k in range(1,int((n-n//2)*n)+1):
	
	square[row][col]=square[row][col]+k
	
	row=row+1
	col=col+1
	
	if col==n:
		col=col-col
	elif row==n:
		row=row-row
	elif square[row][col]!=0:
		
		row=row-1
		col=col-1
		row=row-1	

#second position
row=n-2
col=n-1
	
#second cycle
for k in range((n-n//2)*n+1,n*n+1):
	
	square[row][col]=square[row][col]+k
	
	row=row+1
	col=col+1
	
	if col==n:
		col=col-col
	elif row==n:
		row=row-row	
	
	
	elif square[row][col]!=0:
		
		row=row-1
		col=col-1
		row=row-1

#output
for i in range(n):
	for j in range(n):
		print("%-4d" % square[i][j], end="")

	print()
	
print()

#stop
from os import system
system("pause")
	
	
