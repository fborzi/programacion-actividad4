"""
 Ejercicio 18:
 Función que encuentra dígitos repetidos en un número
"""
from funciones import digitos_repetidos

# === PRUEBAS DE LA FUNCIÓN ===

print("=== DÍGITOS REPETIDOS ===")
print()

# Prueba 1: Número con varios dígitos repetidos
numero1 = 112233
resultado1 = digitos_repetidos(numero1)
print(f"digitos_repetidos({numero1}) = {resultado1}")
print(f"Explicación: El 1, 2 y 3 aparecen más de una vez")
print()

# Prueba 2: Número con un dígito repetido
numero2 = 123451
resultado2 = digitos_repetidos(numero2)
print(f"digitos_repetidos({numero2}) = {resultado2}")
print(f"Explicación: Solo el 1 aparece más de una vez")
print()

# Prueba 3: Número sin dígitos repetidos
numero3 = 12345
resultado3 = digitos_repetidos(numero3)
print(f"digitos_repetidos({numero3}) = {resultado3}")
print(f"Explicación: Ningún dígito se repite")
print()

# Prueba 4: Todos los dígitos iguales
numero4 = 7777
resultado4 = digitos_repetidos(numero4)
print(f"digitos_repetidos({numero4}) = {resultado4}")
print(f"Explicación: El 7 aparece 4 veces, pero solo se lista una vez")
print()

# Prueba 5: Número con varios dígitos repetidos múltiples veces
numero5 = 1122334455
resultado5 = digitos_repetidos(numero5)
print(f"digitos_repetidos({numero5}) = {resultado5}")
print(f"Explicación: Los dígitos 1, 2, 3, 4 y 5 se repiten")
print()

# Prueba 6: Número con ceros
numero6 = 100200
resultado6 = digitos_repetidos(numero6)
print(f"digitos_repetidos({numero6}) = {resultado6}")
print(f"Explicación: El 0 aparece 3 veces")
print()

# Prueba 7: Número de un solo dígito
numero7 = 5
resultado7 = digitos_repetidos(numero7)
print(f"digitos_repetidos({numero7}) = {resultado7}")
print(f"Explicación: No hay repeticiones con un solo dígito")
print()

# === PRUEBA INTERACTIVA ===
print("=" * 50)
print("PRUEBA INTERACTIVA")
print()

try:
    numero_usuario = int(input("Ingrese un número para verificar sus dígitos repetidos: "))
    resultado_usuario = digitos_repetidos(numero_usuario)
    
    if len(resultado_usuario) == 0:
        print(f"El número {numero_usuario} NO tiene dígitos repetidos")
    else:
        print(f"El número {numero_usuario} tiene los siguientes dígitos repetidos: {resultado_usuario}")
except ValueError:
    print("Error: Debe ingresar un número entero válido")