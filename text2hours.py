## counting hours by entering time in a molitary style

## TITLE

print()
print("THIS PROG COUNTS DIURNAL HOURS DIFFERENCE")
print()

#let user input time
userInput1=input("Please, enter time in a military style (like this 0900): ")
userInput2=input("Please, enter second time point (like this 1730): ")




#transform the military style digits to hours and minutes

# first time point
# get the text to integer
hours1 = int (userInput1[0] + userInput1[1])
minutes1 = int (userInput1[2] + userInput1[3])

# get the numbers to 24-hours system in minutes measure

hours1 = hours1 * 24 * 60
minutesTotal1 = hours1 + minutes1





# second time point
# get the text to integer
hours2 = int (userInput2[0] + userInput2[1])
minutes2 = int (userInput2[2] + userInput2[3])

# get the numbers to 24-hours system in minutes measure
hours2 = hours2 * (24*60)
minutesTotal2 = hours2 + minutes2



# count difference
if minutesTotal2>minutesTotal1:
    minutesResult = minutesTotal2 - minutesTotal1
else:
    minutesTotal3 = 24**2*60 - minutesTotal1
    minutesResult = abs(minutesTotal3 + minutesTotal2) 
    

# transform minutes to hours and minutes

hoursResult = int ((minutesResult //60) / 24)
minutesResult = minutesResult % 60
print()
s="_"*45
print(s)
print()
print ("The difference is", hoursResult, "hours", minutesResult, "minutes")




