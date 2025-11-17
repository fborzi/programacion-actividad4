#Lista de elementos

a = [False, 1, 'dos', 3.0, 'ix',(5),[3,3], True]

#Obtener el primer elemento
print('Primero:', a[0])
#Obtener ultimo elemento
print('Ultimo:',a[-1])

#Elimina el primer elemento
print('Lista:',a)
a.pop(0)
print('Lista con el primer elemento eliminado:',a)


#Eliminar los ultimos tres elementos de la lista
print('Lista:',a)
a=a[-3:]
print('Lista sin los ultimos tres elementos:',a)

#insertar el valor 9 en el primer lugar de la lista
print('Lista:',a)
a.insert(0,9)
print('Lista luego de posicionar 9 en el primer lugar de la lista',a)

#remplazar valor por otro
print('Lista:',a)
if 'ix' in a:
    a[a.index('ix')] =4
    print ('ix remplazado',a)


#agrega un valor al final de la lista
print('Lista:',a)
a.append(5)
print('Valor 5 añadido',a)

#primeros tres elementos
print('Lista:',a)
elementos= a[:3] #muestra los 3 primeros elementos de la lista 
print('Luego de eliminar los primeros elementos',elementos)

#Insertar la lista al final de la misma lista, es decir, la lista a deberá contener a la lista a
print('Lista:',a)
a.append(a)
print('Lista luego de insertar la lista',a)

#Determinar si hay elementos que pertenecen a la lista
print('Lista:',a)
if 'dos' in a or 3.0 in a :
    print('Pertenecen')
else:
    print('No pertenecen en la lista.')

#Determinar cuantas veces aparece el elemento 1 y 4 en la lista
print('Lista',a)
print('Cantidad de 1:',a.count(1))
print('Cantidad de 4:',a.count(1))

#Imprimir cada elemento de la lista (iterando) 
print('Lista:',a)
for elemento in a:
    print(elemento)
print('Print iterando:')

#Imprimir cada elemento de la lista en forma inversa (iterando) 
print('Lista:',a)
for elemento in reversed(a):
    print(elemento)


