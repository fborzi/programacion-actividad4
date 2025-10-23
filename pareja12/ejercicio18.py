"""
EJERCICIO 18
Implementá la función digitos_repetidos(n) que, dado un número n, 
retorne una lista conteniendo los dígitos que se repiten en n. 
Cada dígito deberá aparecer una única vez en la lista, 
aunque se repita varias veces.
"""

from funciones import digitos_repetidos

numero = int(input("Ingrese un número para verificar sus digitos repetidos: "))
resultado = digitos_repetidos(numero)
print("Dígitos repetidos:", resultado)