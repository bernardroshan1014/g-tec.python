x=7; y=5; z=9

print('x:', x)
# x: 7

print('y:', y)
# y: 5

print('z:', z)
# z: 9

if x > y and x > z: # 7 >= 5 => True, 7 >9 => False (True and False => False)
    print(f'Biggest value: {x}') # 9
elif y > z: # 5 > 9 => False
    print (f'Biggest value: {y}')
else:
    print(f'Biggest value: {z}') # 9
    