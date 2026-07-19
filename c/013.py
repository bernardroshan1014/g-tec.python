x, y, z=7, 7, 7
# \n escape sequence make a newline
print(f'x: {x}\ny: {y}\nz: {z}')
# x: 7, y: 7, z: 7

if x > y: # 7 > 7 => False
    if x > z:
        print(f'x: {x}')
    else:
        print(f'z: {z}')
else:
    if y > z: # 7 > 7 => False
        print(f'y: {y}')
    else:
        print(f'z: {z}') # z: 7
        

