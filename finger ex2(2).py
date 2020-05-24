'''Write a program that asks the user to input 10 integers, and then
prints the largest odd number that was entered. If no odd number was entered, it
should print a message to that effect.'''


numbers = []

# get user to input 10 integers
for i in range(0, 10):
    numbers.append(int(input("Enter an INT:")))

odd_nums = []
for i in numbers:
    if i%2 != 0 :
        odd_nums.append(i)
if len(odd_nums) == 0:
    print('there is no odd nums')
else:
    print(max(odd_nums))
       
       
       
        
            
    