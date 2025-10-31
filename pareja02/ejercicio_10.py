"""
EJERCICIO 10: Función dígitos
Implementar la función digitos(numero) que retorna una lista con los dígitos
que componen al número.
"""

from funciones import digitos

print("Pruebas de la función digitos():\n")

# Ejemplo 1
numero1 = 18413
resultado1 = digitos(numero1)
print(f"digitos({numero1})")
print(f"Resultado: {resultado1}\n")

# Ejemplo 2
numero2 = 2025
resultado2 = digitos(numero2)
print(f"digitos({numero2})")
print(f"Resultado: {resultado2}\n")

# Ejemplo 3: Número de un solo dígito
numero3 = 7
resultado3 = digitos(numero3)
print(f"digitos({numero3})")
print(f"Resultado: {resultado3}\n")

# Ejemplo 4: Número negativo
numero4 = -456
resultado4 = digitos(numero4)
print(f"digitos({numero4})")
print(f"Resultado: {resultado4} (se toma el valor absoluto)")
