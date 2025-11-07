# Dada la lista a = [ False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True ] utilizar instrucciones que permitan:
# Obtener el primero y el último elemento.
# Eliminar el primer elemento
# Eliminar los tres últimos elementos
# Insertar el valor 9 en el primer lugar de la lista (desplazando al resto)
# Reemplazar el valor 'ix' por el valor 4
# Agregar el valor 5 al final de la lista
# Obtener, mediante una rebanada, los primeros 3 elementos
# Insertar la lista al final de la misma lista, es decir, la lista a deberá contener a la lista a
# Determinar si el elemento ‘dos’ pertenece a la lista y si el elemento 3.0 pertenece a la lista
# Determinar cuántas veces aparece el elemento 1 en la lista y cuántas veces aparece el elemento 4
# Imprimir cada elemento de la lista (iterando)
# Imprimir cada elemento de la lista en forma inversa (iterando)

a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

# a
print("Primer elemento de la lista: ", a[0])
print("Ultimo elemento de la lista: ", a[-1])

# b
print("Lista: ", a)
a.pop(0)
print("Lista luego de eliminar el primer elemento:", a)

# c
print("Lista: ", a)
a = a[:-3]
print("Lista luego de eliminar los ultimos 3 elementos: ", a)

# d
print("Lista: ", a)
a.insert(0, 9)
print("Lista luego de posicionar el valor 9 en el primer lugar de la lista (desplazando al resto): ", a)

# e
print("Lista: ", a)
a[a.index('ix')] = 4
print("Luego de reemplazar el valor 'ix' por el valor 4:", a)

# f
print("Lista: ", a)
a.append(5)
print("Luego de añadir el valor 5 al final de la lista:", a)

# g
print("Lista: ", a)
elementos = a[:3]
print("Luego de slicear los primeros 3 elementos", elementos)

# h
print("Lista: ", a)
a.extend(a)
print("Lista luego de introducir a dentro de a:", a)

# i
print("Lista: ", a)
print("'dos' dentro de la lista: ", 'dos' in a)
print("3.0 dentro de la lista: ", 3.0 in a)

# j
print("Lista: ", a)
print("Lista count '1': ", a.count(1))
print("Lista count '4': ", a.count(4))

# k
print("Lista: ", a)
print("Print iterando: ")
for element in a:
    print(element)

# l
print("Lista: ", a)
print("Print iterando pero al reves: ")
for element in reversed(a):
    print(element)