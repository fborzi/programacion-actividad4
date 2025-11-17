#EJE11

from Funcioness import borrar_adyacentes

print("Pruebas de la función borrar_adyacentes():\n")

# Ejemplo 1
lista1 = ['a', 'a', '*', 'b', '=', '=', 'c', 'a']
resultado1 = borrar_adyacentes(lista1)
print(f"Lista original: {lista1}")
print(f"Resultado:      {resultado1}\n")

# Ejemplo 2
lista2 = ['x', 'x', 'x', 'y', 'z', 'z']
resultado2 = borrar_adyacentes(lista2)
print(f"Lista original: {lista2}")
print(f"Resultado:      {resultado2}\n")

# Ejemplo 3: Sin repeticiones adyacentes
lista3 = ['a', 'b', 'c', 'd']
resultado3 = borrar_adyacentes(lista3)
print(f"Lista original: {lista3}")
print(f"Resultado:      {resultado3}\n")

# Ejemplo 4: Todos iguales
lista4 = ['m', 'm', 'm', 'm']
resultado4 = borrar_adyacentes(lista4)
print(f"Lista original: {lista4}")
print(f"Resultado:      {resultado4}")
