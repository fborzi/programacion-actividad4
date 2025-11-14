# Función dos_minimos

from funciones import dos_minimos

# Pruebas de la función dos_minimos
print("\nPruebas de la función dos_minimos():")

lista1 = [23, 456, 12, 16, -4, 56]
resultado1 = dos_minimos(lista1)
print(f"dos_minimos({lista1}) retorna {resultado1}")

lista2 = [4]
resultado2 = dos_minimos(lista2)
print(f"dos_minimos({lista2}) retorna {resultado2}")

lista3 = []
resultado3 = dos_minimos(lista3)
print(f"dos_minimos({lista3}) retorna {resultado3}")

# Pruebas adicionales
lista4 = [100, 50, 25, 75, 10, 5]
resultado4 = dos_minimos(lista4)
print(f"dos_minimos({lista4}) retorna {resultado4}")