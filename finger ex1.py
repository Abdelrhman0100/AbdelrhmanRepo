''' 
finger excersise 1

Write a program that examines three variables—x, y, and z—and
prints the largest odd number among them. If none of them are odd, it should
print a message to that effect'''  

#using only if else statements



a = int(input('enter the first number: '))
b = int(input('enter the second number: '))
c = int(input('enter the third number: '))


if a%2 != 0 and b%2 != 0 and c%2 != 0 :
    if a>b and a>c:
        print('{} is the largest odd number'.format(a))
    elif b>c:
        print('{} is the largest odd number'.format(b))
    else:
        print('{} is the largest odd number'.format(c))    
elif a%2 != 0 and b%2 != 0 and c%2 == 0 :  
    if  a>b :
        print('{} is the largest odd number'.format(a)) 
    else:
        print('{} is the largest odd number'.format(b)) 
elif a%2 != 0 and b%2 == 0 and c%2 != 0 :
    if a>c:
        print('{} is the largest odd number'.format(a))
    else:
        print('{} is the largest odd number'.format(c))
elif a%2 == 0 and b%2 != 0 and c%2 != 0 : 
    if b>c:
        print('{} is the largest odd number'.format(b))
    else:
        print('{} is the largest odd number'.format(c)) 
elif a%2 != 0 and b%2 == 0 and c%2 == 0 :
    print('{} is the largest odd number'.format(a))

elif a%2 == 0 and b%2 != 0 and c%2 == 0 :
    print('{} is the largest odd number'.format(b))

elif a%2 == 0 and b%2 == 0 and c%2 != 0 :
    print('{} is the largest odd number'.format(c))

else:
    print('there is no odd numbers')                  











'''if x%2 == 0:
    if y%2 == 0:
        if z%2 == 0:
            print ("None of them are odd")
        else:
            print (z)
    elif y > z or z%2 == 0:
        print (y)
    else:
        print (z)
elif y%2 == 0:
    if z%2 == 0 or x > z:
        print (x)
    else:
        print (z)
elif z%2 == 0:
    if x > y:
        print (x)
    else:
        print (y)
else:
    if x > y and x > z:
        print (x)
    elif y > z:
        print (y)
    else:
        print (z)'''        
