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

con_1= 0
con_4= 0

for i in a:
    if i == 1:
        con_1 += 1
    elif i == 4:
        con_4 += 1

print('Hay ', con_1, 'uno(s) en su lista' )
print('Hay ', con_4, 'cuatro(s) en su lista' )


#K

for i in a:
    print(i)


#L
for i in a[::-1]:
    print(i)
