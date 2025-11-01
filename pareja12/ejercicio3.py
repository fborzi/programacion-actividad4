a = [False, 1, "dos", 3.0, "ix", (5,),[3,3], True]

#A

print('el primer elemento de su lista es: ',a[0], ' y el ultimo elemento de su lista es: ', a[-1])

#B
del a[0]


#C

del a[-3:]

#D

a.insert(0,9)


#E
if 'ix' in a:
    i= a.index('ix')
    a[i] = 4


#F
a.append(5)

#G

print(a[0:3])

#H
b= [False, 1, "dos", 3.0, "ix", (5,),[3,3], True]
a.append(b)

#I
numerosAConsultar = [2,3.0]

for i in numerosAConsultar:
    if i in a:
        print('El número ', i, 'pertenece a su lista')
    else: 
        print('El número ', i, 'no pertenece a su lista')


#J


