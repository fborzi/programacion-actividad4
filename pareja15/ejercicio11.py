# Función ocurrencias

from funciones import ocurrencias

# Pruebas de la función ocurrencias
print("\nPruebas de la función ocurrencias():")

lista1 = [1, 1, 2, 2, 2, 3, 1, 1, 1]
resultado1 = ocurrencias(lista1)
print(f"ocurrencias({lista1})")
print(f"retorna: {resultado1}")

lista2 = ['a', 'a', 'b', 'c', 'c', 'c', 'a']
resultado2 = ocurrencias(lista2)
print(f"\nocurrencias({lista2})")
print(f"retorna: {resultado2}")

lista3 = [5, 5, 5, 5]
resultado3 = ocurrencias(lista3)
print(f"\nocurrencias({lista3})")
print(f"retorna: {resultado3}")

lista4 = [1, 2, 3, 4, 5]
resultado4 = ocurrencias(lista4)
print(f"\nocurrencias({lista4})")
print(f"retorna: {resultado4}")