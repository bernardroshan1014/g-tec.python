x, y, z=5, 9, 7
# \n escape sequence make a newline
print(f'x: {x}\ny: {y}\nz: {z})
# x: 5. y: 9, z: 7

if x > y: # 5 > 9 => False
    if x > z:
        print(f'x: {x}')
    else:
        print(f'z: {z}')
else:
    if y > z: # 9 > 7 => True
        print(f'y: {y}') # y: 9
    else:
        print(f'z: {z}')
        
