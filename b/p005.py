def square():
    
    x=0 #declare or create a variable
    
    try:
        #x=input('Enter x value:')
        #x=int(x)
        #OR
        x=int(input('Enter x value: '))
        print(x, 'Square:', x * x)
        return #jump statement terminate a function
    except Exception as e:
        print('Err.:',e)
        return #jump statement terminate a function
    print('Indentation  of square function')
    del x
    
square()

#way-1
#Enter x value: 5
#5 Square: 25

#way-2
#Enter x value: frog
#Err.: invalid literal for int() with base 10: 'frog'