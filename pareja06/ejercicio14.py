"""
EJERCICIO 14: Función dos sumandos
Implementar la función dos_sumandos(lista, resultado) que retorna los índices
de dos elementos cuya suma da el resultado esperado.
"""
from funciones import dos_sumandos

# === PRUEBAS DE LA FUNCIÓN ===

print("=== DOS SUMANDOS ===")
print()

# Prueba 1: Ejemplo del enunciado
lista1 = [2, 7, 11, 15]
objetivo1 = 17
resultado1 = dos_sumandos(lista1, objetivo1)
print(f"Lista: {lista1}")
print(f"Objetivo: {objetivo1}")
print(f"dos_sumandos({lista1}, {objetivo1}) = {resultado1}")
print(f"Verificación: lista[{resultado1[0]}] + lista[{resultado1[1]}] = {lista1[resultado1[0]]} + {lista1[resultado1[1]]} = {lista1[resultado1[0]] + lista1[resultado1[1]]}")
print()

# Prueba 2: Otro ejemplo
lista2 = [3, 2, 4]
objetivo2 = 6
resultado2 = dos_sumandos(lista2, objetivo2)
print(f"Lista: {lista2}")
print(f"Objetivo: {objetivo2}")
print(f"dos_sumandos({lista2}, {objetivo2}) = {resultado2}")
if resultado2:
    print(f"Verificación: lista[{resultado2[0]}] + lista[{resultado2[1]}] = {lista2[resultado2[0]]} + {lista2[resultado2[1]]} = {lista2[resultado2[0]] + lista2[resultado2[1]]}")
print()

# Prueba 3: Con números negativos
lista3 = [1, -3, 5, 7, -1]
objetivo3 = 4
resultado3 = dos_sumandos(lista3, objetivo3)
print(f"Lista: {lista3}")
print(f"Objetivo: {objetivo3}")
print(f"dos_sumandos({lista3}, {objetivo3}) = {resultado3}")
if resultado3:
    print(f"Verificación: lista[{resultado3[0]}] + lista[{resultado3[1]}] = {lista3[resultado3[0]]} + {lista3[resultado3[1]]} = {lista3[resultado3[0]] + lista3[resultado3[1]]}")
print()

# Prueba 4: No existe solución
lista4 = [1, 2, 3]
objetivo4 = 10
resultado4 = dos_sumandos(lista4, objetivo4)
print(f"Lista: {lista4}")
print(f"Objetivo: {objetivo4}")
print(f"dos_sumandos({lista4}, {objetivo4}) = {resultado4}")
print("(No hay dos números que sumen 10)")
print()

# Prueba 5: Mismo número en diferentes posiciones
lista5 = [3, 3, 6]
objetivo5 = 6
resultado5 = dos_sumandos(lista5, objetivo5)
print(f"Lista: {lista5}")
print(f"Objetivo: {objetivo5}")
print(f"dos_sumandos({lista5}, {objetivo5}) = {resultado5}")
if resultado5:
    print(f"Verificación: lista[{resultado5[0]}] + lista[{resultado5[1]}] = {lista5[resultado5[0]]} + {lista5[resultado5[1]]} = {lista5[resultado5[0]] + lista5[resultado5[1]]}")