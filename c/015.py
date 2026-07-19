for i in range(1, 10):
    if i > 5: #6 > 5
        break # jump statement terminate a loop
    
    print(i) # 1 to 5

else:
    print('End of loop, i:', i)

print('Main block, i:', i) # Main block, i: 6