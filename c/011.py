x, y, z=7, 5, 9
# \n escape sequence make a newline
print(f'x: {x}\ny: {y}\nz: {z}')
# x: 7, y: 5, z: 9

if x > y: # 7 > 5 => True
    if x > z: # 7 > 9 => False
        print(f'x: {x}')
    else:
        print(f'z: {z}') # z: 9
else:
    if y > z:
        print(f'y: {y}')
    else:
        print(f'z: {z}')
        
