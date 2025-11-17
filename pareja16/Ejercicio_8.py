
from funciones import piedra_papel_tijera

jug1 = input("Jugador 1 elige (piedra/papel/tijera): ")
jug2 = input("Jugador 2 elige (piedra/papel/tijera): ")

resultado = piedra_papel_tijera(jug1, jug2)

if resultado == 0:
    print("Empate.")
elif resultado == 1:
    print("Gana el jugador 1.")
else:
    print("Gana el jugador 2.")

