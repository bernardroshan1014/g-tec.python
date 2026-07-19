i=0
while i < 10:
    if i > 4: # 5 > 4
        break
    
    print('1:',i) # 0, 1, 2, 3, 4
    i += 1

else:
    print('End of loop, i', i)

print('Main block, i:', i) # Main block, i: 5
