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
    finally:
        print('Indentation  of finally')
        del x
    
square()

#way-1
#Enter x value: 8
#8 Square: 64
#Indentation  of finally

#way-2
#Enter x value: wolf
#Err.: invalid literal for int() with base 10: 'wolf'
#Indentation  of finally