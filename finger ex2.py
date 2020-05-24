# using while loop write a program taking an input number of how many times to print "X"


numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
while(len(toPrint)<numXs):
    toPrint += 'x'
print(toPrint)    
