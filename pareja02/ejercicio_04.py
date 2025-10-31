"""
EJERCICIO 4: Operaciones con listas
Dada la lista a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]
Realizar diversas operaciones sobre la lista
"""

# Lista original
a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

print("Lista original:")
print(a)
print("\n" + "="*60)

# a) Obtener el primero y el último elemento
print("\na) Primero y último elemento:")
primero = a[0]
ultimo = a[-1]
print(f"   Primero: {primero}")
print(f"   Último: {ultimo}")

# b) Eliminar el primer elemento
print("\nb) Eliminar el primer elemento:")
a.pop(0)
print(f"   Lista después: {a}")

# c) Eliminar los tres últimos elementos
print("\nc) Eliminar los tres últimos elementos:")
del a[-3:]
print(f"   Lista después: {a}")

# d) Insertar el valor 9 en el primer lugar
print("\nd) Insertar el valor 9 en el primer lugar:")
a.insert(0, 9)
print(f"   Lista después: {a}")

# e) Reemplazar el valor 'ix' por el valor 4
print("\ne) Reemplazar 'ix' por 4:")
indice_ix = a.index('ix')
a[indice_ix] = 4
print(f"   Lista después: {a}")

# f) Agregar el valor 5 al final
print("\nf) Agregar el valor 5 al final:")
a.append(5)
print(f"   Lista después: {a}")

# g) Obtener los primeros 3 elementos mediante rebanada
print("\ng) Primeros 3 elementos (rebanada):")
primeros_tres = a[:3]
print(f"   {primeros_tres}")

# h) Insertar la lista al final de sí misma
print("\nh) Insertar la lista al final de sí misma:")
a.append(a[:])  # Usamos a[:] para hacer una copia
print(f"   Lista después: {a}")

# i) Determinar si 'dos' y 3.0 pertenecen a la lista
print("\ni) Verificar pertenencia:")
print(f"   'dos' pertenece a la lista: {'dos' in a}")
print(f"   3.0 pertenece a la lista: {3.0 in a}")

# j) Contar ocurrencias de 1 y 4
print("\nj) Contar ocurrencias:")
print(f"   El elemento 1 aparece {a.count(1)} veces")
print(f"   El elemento 4 aparece {a.count(4)} veces")

# k) Imprimir cada elemento iterando
print("\nk) Imprimir cada elemento (iterando):")
for i, elemento in enumerate(a):
    print(f"   Índice {i}: {elemento}")

# l) Imprimir cada elemento en forma inversa
print("\nl) Imprimir cada elemento en forma inversa:")
for i, elemento in enumerate(reversed(a)):
    print(f"   Posición desde el final {i}: {elemento}")
