"""
EJERCICIO 8: Piedra, papel o tijera
Implementar la función piedra_papel_tijera(uno, dos) que determina el ganador.
Retorna 1 si gana el jugador 1, 2 si gana el jugador 2, 0 si hay empate.
"""
from funciones import piedra_papel_tijera

# === PRUEBAS DE LA FUNCIÓN ===

print("=== JUEGO: PIEDRA, PAPEL O TIJERA ===")
print()

# Prueba 1: Jugador 1 elige piedra, Jugador 2 elige tijera
resultado = piedra_papel_tijera("piedra", "tijera")
print(f"piedra_papel_tijera('piedra', 'tijera') = {resultado} (Gana jugador 1 - Piedra rompe Tijera)")

# Prueba 2: Jugador 1 elige tijera, Jugador 2 elige papel
resultado = piedra_papel_tijera("tijera", "papel")
print(f"piedra_papel_tijera('tijera', 'papel') = {resultado} (Gana jugador 1 - Tijera corta Papel)")

# Prueba 3: Jugador 1 elige papel, Jugador 2 elige piedra
resultado = piedra_papel_tijera("papel", "piedra")
print(f"piedra_papel_tijera('papel', 'piedra') = {resultado} (Gana jugador 1 - Papel envuelve Piedra)")

# Prueba 4: Jugador 1 elige piedra, Jugador 2 elige papel
resultado = piedra_papel_tijera("piedra", "papel")
print(f"piedra_papel_tijera('piedra', 'papel') = {resultado} (Gana jugador 2 - Papel envuelve Piedra)")

# Prueba 5: Empate
resultado = piedra_papel_tijera("tijera", "tijera")
print(f"piedra_papel_tijera('tijera', 'tijera') = {resultado} (Empate)")

# Prueba 6: Ignorando mayúsculas
resultado = piedra_papel_tijera("PIEDRA", "TiJeRa")
print(f"piedra_papel_tijera('PIEDRA', 'TiJeRa') = {resultado} (Gana jugador 1 - Ignora mayúsculas)")

print()
print("=== JUEGO INTERACTIVO ===")

# Versión interactiva para jugar
jugador1 = input("Jugador 1, ingrese su elección (piedra/papel/tijera): ")
jugador2 = input("Jugador 2, ingrese su elección (piedra/papel/tijera): ")

ganador = piedra_papel_tijera(jugador1, jugador2)

print()
if ganador == 0:
    print("¡EMPATE! Ambos eligieron lo mismo.")
elif ganador == 1:
    print(f"¡GANA JUGADOR 1! {jugador1.capitalize()} vence a {jugador2.capitalize()}")
else:
    print(f"¡GANA JUGADOR 2! {jugador2.capitalize()} vence a {jugador1.capitalize()}")