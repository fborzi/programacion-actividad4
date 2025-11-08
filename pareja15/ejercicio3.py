# Operaciones avanzadas con listas
# Lista original
a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]
print(f"\nLista original: {a}")
# Obtener el primero y el último elemento
print("\na) Primero y último elemento:")
primero = a[0]
ultimo = a[-1]
print(f"Primero: {primero}")
print(f"Último: {ultimo}")

# Eliminar el primer elemento
print("\nb) Eliminar el primer elemento:")
a.pop(0)
print(f"Lista después de eliminar el primero: {a}")

# Eliminar los tres últimos elementos
print("\nc) Eliminar los tres últimos elementos:")
del a[-3:]
print(f"Lista después de eliminar los últimos 3: {a}")

# Insertar el valor 9 en el primer lugar
print("\nd) Insertar 9 en el primer lugar:")
a.insert(0, 9)
print(f"Lista después de insertar 9 al inicio: {a}")

# Reemplazar 'ix' por 4
print("\ne) Reemplazar 'ix' por 4:")
if 'ix' in a:
    indice = a.index('ix')
    a[indice] = 4
print(f"Lista después de reemplazar 'ix' por 4: {a}")

# Agregar el valor 5 al final
print("\nf) Agregar 5 al final:")
a.append(5)
print(f"Lista después de agregar 5 al final: {a}")

# Obtener los primeros 3 elementos mediante rebanada
print("\ng) Primeros 3 elementos (rebanada):")
primeros_tres = a[:3]
print(f"Primeros 3 elementos: {primeros_tres}")

# Insertar la lista al final de sí misma
print("\nh) Insertar la lista al final de sí misma:")
a.append(a[:])  # Usamos a[:] para hacer una copia
print(f"Lista después de insertarse a sí misma: {a}")

# Determinar si 'dos' y 3.0 pertenecen a la lista
print("\ni) Verificar pertenencia:")
print(f"¿'dos' pertenece a la lista? {('dos' in a)}")
print(f"¿3.0 pertenece a la lista? {(3.0 in a)}")

# Contar apariciones de 1 y 4
print("\nj) Contar apariciones:")
print(f"El elemento 1 aparece {a.count(1)} veces")
print(f"El elemento 4 aparece {a.count(4)} veces")

# Imprimir cada elemento iterando
print("\nk) Imprimir cada elemento:")
for elemento in a:
    print(elemento)

# Imprimir cada elemento en forma inversa
print("\nl) Imprimir cada elemento en forma inversa:")
for elemento in reversed(a):
    print(elemento)