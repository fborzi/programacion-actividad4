#EJE9

from Funcioness import piedra_papel_tijera

print("Juego: Piedra, Papel o Tijera")
print("="*50)

# Pruebas de la función
pruebas = [
    ("piedra", "tijera"),
    ("tijera", "papel"),
    ("papel", "piedra"),
    ("piedra", "piedra"),
    ("papel", "tijera"),
    ("PIEDRA", "tijera"),  # Prueba con mayúsculas
]

for jugador1, jugador2 in pruebas:
    resultado = piedra_papel_tijera(jugador1, jugador2)
    
    print(f"\nJugador 1: {jugador1.upper()}")
    print(f"Jugador 2: {jugador2.upper()}")
    
    if resultado == 0:
        print("Resultado: EMPATE")
    elif resultado == 1:
        print("Resultado: Gana JUGADOR 1")
    else:
        print("Resultado: Gana JUGADOR 2")

# Modo interactivo
print("\n" + "="*50)
print("Modo interactivo:")
print("="*50)

jugador1 = input("Jugador 1, elige (piedra/papel/tijera): ")
jugador2 = input("Jugador 2, elige (piedra/papel/tijera): ")

resultado = piedra_papel_tijera(jugador1, jugador2)

print("\n" + "-"*50)
if resultado == 0:
    print("¡EMPATE!")
elif resultado == 1:
    print("¡GANA JUGADOR 1!")
else:
    print("¡GANA JUGADOR 2!")
