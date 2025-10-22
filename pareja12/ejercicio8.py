"""
“Piedra, papel o tijera” es un juego de manos en el cual existen tres elementos: 
la piedra que vence a la tijera rompiéndola, la tijera que vence al papel cortándolo 
y el papel que vence a la piedra envolviéndola. 
Escribí la función piedra_papel_tijera(uno, dos) que reciba dos cadenas 
como parámetros, donde cada una podrá ser 'piedra', 'papel' o 'tijera' 
(ignorando mayúsculas y minúsculas), las cuales representan los elementos 
elegidos por dos jugadores. La función debe retornar 1 si ganó el primer 
jugador, 2 si ganó el segundo o 0 si hubo empate 
(ambos eligieron el mismo elemento).
"""

from funciones import pieda_papel_tijera
import random

opciones = ['piedra', 'papel', 'tijera']

for i in range (5):
    jugador1 = random.choice(opciones)
    jugador2 = random.choice(opciones)
    resultado = pieda_papel_tijera(jugador1, jugador2)

    print("Partida", i+1)
    print(" Jugador 1:", jugador1)
    print(" Jugador 2:", jugador2)

    if resultado == 0:
        print("Empate.")
    elif resultado == 1:
        print("Ganó el Jugador 1")
    else:
        print("Ganó el Jugador 2")
    print()