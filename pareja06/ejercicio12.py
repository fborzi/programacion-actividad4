"""
EJERCICIO 12: Función sumatoria de dígitos
Implementar las funciones suma_digitos(n) y sumatoria_digitos(lista).
"""

from funciones import suma_digitos, sumatoria_digitos

# === PRUEBAS DE LA FUNCIÓN ===

print("=== SUMATORIA DE DÍGITOS ===")
print()

# Prueba 1: Ejemplo del enunciado
entrada1 = [154, 27890, 111, 43]
salida1 = sumatoria_digitos(entrada1)
print(f"sumatoria_digitos({entrada1})")
print(f"Resultado: {salida1}")
print()
print("Explicación:")
print(f"  154 → 1+5+4 = 10")
print(f"  27890 → 2+7+8+9+0 = 26")
print(f"  111 → 1+1+1 = 3")
print(f"  43 → 4+3 = 7")
print()

# Prueba 2: Números de un solo dígito
entrada2 = [5, 8, 3]
salida2 = sumatoria_digitos(entrada2)
print(f"sumatoria_digitos({entrada2}) = {salida2}")
print()

# Prueba 3: Con ceros
entrada3 = [100, 2005, 30]
salida3 = sumatoria_digitos(entrada3)
print(f"sumatoria_digitos({entrada3}) = {salida3}")
print(f"Explicación:")
print(f"  100 → 1+0+0 = 1")
print(f"  2005 → 2+0+0+5 = 7")
print(f"  30 → 3+0 = 3")
print()

# Prueba 4: Lista vacía
entrada4 = []
salida4 = sumatoria_digitos(entrada4)
print(f"sumatoria_digitos({entrada4}) = {salida4}")
print()

# === PRUEBA DE suma_digitos INDIVIDUAL ===
print("=== PRUEBAS DE suma_digitos ===")
print(f"suma_digitos(154) = {suma_digitos(154)}")
print(f"suma_digitos(27890) = {suma_digitos(27890)}")
print(f"suma_digitos(999) = {suma_digitos(999)}")