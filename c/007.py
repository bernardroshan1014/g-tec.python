x=5; y=9; z=7

print('x:', x)
# x:5

print('y:', y)
# y:9

print('z:', z)
# z:7

if x > y and x > z: # 5 > 9 => False
    print(f'Biggest value: {x}') # formatted string syntax f'<constant value> {variable-name}}'
elif y > z: # 9 > 7 => True
    print (f'Biggest value: {y}') # 9
else:
    print(f'Biggest value: {z}')