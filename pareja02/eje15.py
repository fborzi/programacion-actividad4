#EJER15

from Funcioness import dos_sumandos

print("Pruebas de la función dos_sumandos():\n")

# Ejemplo 1
lista1 = [2, 7, 11, 15]
objetivo1 = 17
resultado1 = dos_sumandos(lista1, objetivo1)
print(f"Lista: {lista1}")
print(f"Objetivo: {objetivo1}")
print(f"Resultado: {resultado1}")
if resultado1:
    print(f"Verificación: lista[{resultado1[0]}] + lista[{resultado1[1]}] = {lista1[resultado1[0]]} + {lista1[resultado1[1]]} = {lista1[resultado1[0]] + lista1[resultado1[1]]}\n")

# Ejemplo 2
lista2 = [3, 2, 4]
objetivo2 = 6
resultado2 = dos_sumandos(lista2, objetivo2)
print(f"Lista: {lista2}")
print(f"Objetivo: {objetivo2}")
print(f"Resultado: {resultado2}")
if resultado2:
    print(f"Verificación: lista[{resultado2[0]}] + lista[{resultado2[1]}] = {lista2[resultado2[0]]} + {lista2[resultado2[1]]} = {lista2[resultado2[0]] + lista2[resultado2[1]]}\n")

# Ejemplo 3: No hay solución
lista3 = [1, 2, 3]
objetivo3 = 10
resultado3 = dos_sumandos(lista3, objetivo3)
print(f"Lista: {lista3}")
print(f"Objetivo: {objetivo3}")
print(f"Resultado: {resultado3}")
print("(No hay dos números que sumen 10)")
