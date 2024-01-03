x = '*'
y = ' '
print('Figure N°2 :')    
print()
for i in range(5,0,-1):
    print(x * i)
print()

print('Figure N°3 :')
print()
for i in range(1,6):
    print(x * i)
print()

print('Figure N°4 :')
print()
for i in range(5,0,-1):
    print( (y * (5 - i)) + (x * i) )
print()

print('Figure N°5 :')
print()
for i in range(1,6):  
    print(x * i)
for i in range(4,0,-1):  
    print(x * i)
print()

print('Figure N°6 :')
print()
for i in range(5,0,-1):  
    print(x * i)
for i in range(2,6):  
    print(x * i)
print()

print('Figure N°7 :')
print()
for i in range(1,6):
    print( (y * (5 - i)) + (x * i) )

for i in range(4,0,-1):
    print( (y * (5 - i)) + (x * i) )
print()

print('Figure N°8 :')
print()
for i in range(5,0,-1):
    print( (y * (5 - i)) + (x * i) )

for i in range(2,6):
    print( (y * (5 - i)) + (x * i) )
print()

print('Figure N°9 :')
print()
for i in range(1,6):
        print( (y * (5 - i)) + (x * i ) + (x * (i - 1)) + (y * (5 - i)))
print()

print('Figure N°12 :')
print()
for i in range(5,0,-1):
    print( (y * (5 - i)) + (x * i ) + (x * (i - 1)) + (y * (5 - i)))
for i in range(2,6):
    print( (y * (5 - i)) + (x * i ) + (x * (i - 1)) + (y * (5 - i)))
print()

print('Figure N°13 :')
print()
for i in range(0,5):
    print( (x * (i + 1)) + (y * ( 10 - ((i * 2) + 2))) + (x * (i + 1)))
print()

print('Figure N°14 :')
print()
for i in range(4,-1,-1):
    print( (x * (i + 1)) + (y * ( 10 - ((i * 2) + 2))) + (x * (i + 1)))
print()

print('Figure N°15 :')
print()
for i in range(0,4):
    print( (x * (i + 1)) + (y * ( 10 - ((i * 2) + 2))) + (x * (i + 1)))
for i in range(4,-1,-1):
    print( (x * (i + 1)) + (y * ( 10 - ((i * 2) + 2))) + (x * (i + 1)))
print()

print('Figure N°16 :')
print()
for i in range(4,-1,-1):
    print( (x * (i + 1)) + (y * ( 10 - ((i * 2) + 2))) + (x * (i + 1)))
for i in range(0,4):
    print( (x * (i + 1)) + (y * ( 10 - ((i * 2) + 2))) + (x * (i + 1)))
print()

print('Figure N°17 :')
print()
for i in range(0,5):
    if i == 0:
        print( x  )
    elif i == 4:
        print( x * ( i + 1) )
    else:
        print( x  + ( y * ( i - 1) ) + x )
print()

print('Figure N°18 :')
print()
for i in range(4,-1 ,-1):
    if i == 0:
        print( x )
    elif i == 4:
        print( x * ( i + 1) )
    else:
        print( x  + ( y * ( i - 1) ) + x )
print()


print('Figure N°19 :')
print()
for i in range(0,5):
    if i == 0:
        print((y * (4 - i)) + x )
    elif i == 4:
        print( x * ( i + 1) )
    else:
        print( (y * (4 - i)) + x  + ( y * (i - 1 ) ) + x )
print()


print('Figure N°22 :')
print()
for i in range(4,-1 ,-1):
    if i == 0:
        print( x )
    elif i == 4:
        print( x * ( i + 1) )
    else:
        print( x  + ( y * ( i - 1) ) + x )
for i in range(1,5):
    if i == 4:
        print( x * ( i + 1) )
    else:
        print( x  + ( y * ( i - 1) ) + x )

print('Figure N°23 :')
print()
for i in range(0,5):
    if i == 0:
        print((y * (4 - i)) + x )
    else:
        print( (y * (4 - i)) + x  + ( y * (i - 1 ) ) + x )

for i in range(3,-1,-1):
    if i == 0:
        print((y * (4 - i)) + x )
    else:
        print( (y * (4 - i)) + x  + ( y * (i - 1 ) ) + x )
print()

print('Figure N°24 :')
print()

for i in range(4,-1,-1):
    if i == 4:
        print( x * ( i + 1) )
    elif i == 0:
        print((y * (4 - i)) + x )
    else:
        print( (y * (4 - i)) + x  + ( y * (i - 1 ) ) + x )
for i in range(1,5):
    if i == 0:
        print((y * (4 - i)) + x )
    elif i == 4:
        print( x * ( i + 1) )
    else:
        print( (y * (4 - i)) + x  + ( y * (i - 1 ) ) + x )
print()


print('Figure N°25 :')
print()
for i in range(0,5):            
        if i == 0:
            print( (y * (4 - i)) + x + (y * (4 - i) ) )  
        elif i == 4:
            print(x * (i + 5))   
        else:
            print( (y * (4 - i)) + x + (y * (i + (i - 1)) + x + (y * (4 - i) ) ) ) 
print()

print('Figure N°26 :')
print()
for i in range(4,-1,-1):            
        if i == 0:
            print( (y * (4 - i)) + x + (y * (4 - i) ) )  
        elif i == 4:
            print(x * (i + 5))   
        else:
            print( (y * (4 - i)) + x + (y * (i + (i - 1)) + x + (y * (4 - i) ) ) ) 
print()

print('Figure N°27 :')
print()
for i in range(0,5):            
        if i == 0:
            print( (y * (4 - i)) + x + (y * (4 - i) ) )   
        else:
            print( (y * (4 - i)) + x + (y * (i + (i - 1)) + x + (y * (4 - i) ) ) ) 
for i in range(4,-1,-1):            
        if i == 0:
            print( (y * (4 - i)) + x + (y * (4 - i) ) )  
        else:
            print( (y * (4 - i)) + x + (y * (i + (i - 1)) + x + (y * (4 - i) ) ) ) 

print()


print('Figure N°28 :')
print()
for i in range(4,-1,-1):            
        if i == 0:
            print( (y * (4 - i)) + x + (y * (4 - i) ) )  
        elif i == 4:
            print(x * (i + 5))   
        else:
            print( (y * (4 - i)) + x + (y * (i + (i - 1)) + x + (y * (4 - i) ) ) ) 

for i in range(0,5):            
        if i == 0:
            print( (y * (4 - i)) + x + (y * (4 - i) ) )  
        elif i == 4:
            print(x * (i + 5))   
        else:
            print( (y * (4 - i)) + x + (y * (i + (i - 1)) + x + (y * (4 - i) ) ) ) 
print()

print('Figure N°29 :')
print()
for i in range(5):
    print(x*5)


