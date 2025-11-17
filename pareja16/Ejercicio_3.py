
a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

# a) Obtener el primero y el último elemento

print("El primer elemento es: ", a[0])
print("El último elemento es: ", a[-1])

# b) Eliminar el primer elemento

a.pop(0)
print("Lista luego de eliminar el primer elemento: ", a)

# c) Eliminar los tres últimos elementos

del a[-3:]
print("Lista luego de eliminar los tres últimos elementos: ", a)

# d) Insertar el valor 9 en el primer lugar
a.insert(0, 9)

print("Lista luego de insertar el valor 9 al inicio: ", a)

# e) Reemplazar el valor 'ix' por el valor 4
indice = a.index('ix')
a[indice] = 4
print("Lista luego de reemplazar 'ix' por 4: ", a)

# f) Agregar el valor 5 al final
a.append(5)
print("Lista luego de agregar el valor 5 al final: ", a)

# g) Obtener, mediante una rebanada, los primeros 3 elementos

print(" Los primeros 3 elementos son: ", a[:3])

# h) Insertar la lista al final de sí misma
a.extend(a)
print(" Lista luego de insertarse al final de sí misma: ", a)

# i) Determinar si 'dos' y 3.0 pertenecen a la lista

print(" ¿El elemento 'dos' está en la lista?:", 'dos' in a)
print(" ¿El elemento 3.0 está en la lista?:", 3.0 in a)

# j) Contar cuántas veces aparecen 1 y 4

print(" El elemento 1 aparece: ", a.count(1), " veces.")
print(" El elemento 4 aparece: ", a.count(4), " veces.")

# k) Imprimir cada elemento de la lista (iterando)

print(" Elementos de la lista uno por uno:")
for elemento in a:

    print(elemento)

# l) Imprimir cada elemento de la lista en forma inversa (iterando)

a_inversa = a[::-1]

print("Elementos de la lista invertida: ")

for e in a_inversa:
    print(e)



