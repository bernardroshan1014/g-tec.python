try:
    print('Indentation: Try before raise error')
    print(10/0)
    print('Indentation: Try after raise error')

except:
    print('Indentation: Except')

else:
    print('Indentation: Try...Else...')

finally:
    print('Indentation: Finally')