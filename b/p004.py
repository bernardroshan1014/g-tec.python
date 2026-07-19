def square():
    x=int(input('Enter x value: '))
    
    print(x, 'Square:', x * x)
    del x
    return
square()

#way-1
#Enter x value: 6
#6 Square: 36

#way-2
# Enter x value: fow
# ValueError: invalid literal for int() with base 10: 'fow'