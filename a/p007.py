print(range(1,10))
#range(1, 10)

print(list(range(1, 10)))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(tuple(range(1, 10)))
#(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(set(range(1, 10)))
#{1, 2, 3, 4, 5, 6, 7, 8, 9}

print(list(range(1, 10,2)))
#[1, 3, 5, 7, 9]

print(list(range(9, 0, -2)))
#[9, 7, 5, 3, 1]

print(list(range(12, 0, -2)))
#[12, 10, 8, 6, 4, 2]

print(list(range(0, 10, 2)))
#[0, 2, 4, 6, 8]

i=5
print(i)
#5

print(id(i))
#140729559971064                                              

i=9
print(i)
#9

print(id(i))
#140729559971192

w='Orange'

s="Have a nice day"

p="""Have a good  mmorning
Have a good afternoon
Have a good evening
Have a good night"""

print(w)
#Orange

print(s)
#Have a nice day

print(p)
#Have a good  mmorning
#Have a good afternoon
#Have a good evening
#Have a good night

print(id(w))
#2259957325648

w='Grapes'

print(w)
#

print(id(w))
#

L=[]

print(L)
#

L.append('aa')
L.append('cc')
L.append('ee')

print(L)
#

print(id(L))
#

print(L)
#

L=[]

print(L)
#

L.append('aa')
L.append('cc')
L.append('ee')

print(L)
#

print(L[1])
#cc

L.insert(1, 'bb')

print(L)
#
