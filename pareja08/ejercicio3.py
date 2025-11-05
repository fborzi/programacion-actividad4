#a)Obtener el primero y el último elemento.
a = [ False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True ]
print("El primer valor es:",a[0])
print("El ultimo valor es:",a[-1])
#b)Eliminar el primer elemento
del a[0]
print("Los valores del array actualizado",a)
#c)Eliminar los ultimos tres valores del array
del a[-3:]
print("Los valores del array actualizado",a)
#d)Insertar el valor 9 en el primer lugar de la lista (desplazando al resto)
a.insert(0,9)
print("Los valores del array actualizado",a)
#e)Reemplazar el valor 'ix' por el valor 4
if "ix" in a:
   datoIX=a.index("ix")
   a[datoIX]=4;
   print("Los valores del array acualizado",a)
else:
    print("El valor 'ix' no existe en el array")
#f)Agregar el valor 5 al final de la lista
a.append(5)
print("Los valores del array actualizado",a)
#g)Obtener, mediante una rebanada, los primeros 3 elementos
valor=a[:3]
print("Los primeros 3 valores son:",valor)
#h)Insertar la lista al final de la misma lista, es decir, la lista a deberá contener a la lista a
a.extend(a)
print("Los valores del array actualizado",a)
#i) Determinar si el elemento ‘dos’ pertenece a la lista y si el elemento 3.0 pertenece a la lista
print("El valor 'dos'pertenece al array?","dos"in a)
print("El valor '3.0'pertenece al array?",3.0 in a)
#j)Determinar cuántas veces aparece el elemento 1 en la lista y cuántas veces aparece el elemento 4
valor=a.count(1)
valor1=a.count(4)
print("El elemento 1 aparece:",valor)
print("El elemento 4 aparece:",valor1)
#k) Imprimir cada elemento de la lista (iterando)
print("Mostrar los elementos del array interando")
for i in a:
    print(i)
#l)Imprimir cada elemento de la lista en forma inversa (iterando)
print("Mostrar los elementos del array interando, de reversa")
for i in reversed(a):
    print(i)