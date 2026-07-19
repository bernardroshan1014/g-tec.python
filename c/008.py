x=9; y=7; z=5

print('x:', x)
# x: 9

print('y:', y)
# y: 7

print('z:', z)
# z: 5

if x > y and x > z: # 9 > 7 => True, 9 > 5 => True (True and True = True)
    print(f'Biggest value: {x}') # 9
elif y > z:
    print (f'Biggest value: {y}')
else:
    print(f'Biggest value: {z}')