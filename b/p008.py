L=[11, 33, 55]
T=(10, 30, 50)

print(L)
#[11, 33, 55]

print(type(L))
#<class 'list'>

print(len(L))
#3

L.append(66)

print(L)
#[11, 33, 55, 66]

print(type(L))
#<class 'list'>

print(len(L))
#4

L.insert(1, 22)

print(L)
#[11, 22, 33, 55, 66]

print(type(L))
#<class 'list'>

print(len(L))
#5

L.remove(22)

print(L)
#[11, 33, 55, 66]

print(type(L))
#<class 'list'>

print(len(L))
#4

L[2]=44

print(L)
#[11, 33, 44, 66]

print(type(L))
#<class 'list'>

print(len(L))
#4

print(T)
#(10, 30, 50)

print(type(T))
#<class 'tuple'>

print(len(T))
#3

#T[1]=20

#TypeError: 'tuple' object does not support item assignment

print(T[1])

#30

#operator: slice [starting-index, stop-index]

#starting -index: 0

#stop-index: 1

print(T[0:1]) #1 - 0 = 1
#10 = 1

#(10,)

print(T[2:3]) #3 - 2 = 1

#(50,)

print(T[1:2]) # 2 - 1 = 1

#(30,)

S={11, 22, 33, 22, 11, 44}

print(type(S))
#<class 'set'>

print(S)

#{33, 11, 44, 22}

print(len(S))
#4

#er: examresult

er={'rno': 1001, 'sname': 'x5', 'm1': 56.5, 'm2': 63}

print(er)
#{'rno': 1001, 'sname': 'x5', 'm1': 56.5, 'm2': 63)

print(type(er))

#<class 'dict'>

print(len(er))
#4

print(er['rno'])

#1001

print(er['sname'])

#x5

print(er['m1'])

#56.5

print(er['m2'])
#63

print(er.keys())

#dict_keys(['rno', 'sname', 'm1', 'm2'])

print(er.values())

#dict_values([1001, 'x5', 56.5, 63])

er['total']=er['m1'] + er['m2']
er['avg']=er['total'] / 2

if er['m1'] > 34.4 and er['m2'] > 34.4:
    er['result']='Pass'

else:

    er['result']='Fail'

print(er)

#{'rno': 1001, 'sname': 'x5', 'm1': 56.5, 'm2': 63, 'total': 119.5, 'avg': 59.75, 'result': 'Pass'}
