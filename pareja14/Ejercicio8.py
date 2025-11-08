from Funciones import piedra_papel_tijera
print("vamos a jugar el juego de 'piedra-papel-tijera'")
jugador1 = input("ingrese 1 de las 3 opciones (piedra-papel-tijera): ")
print("\n" * 100)
jugador2 = input("ingrese 1 de las 3 opciones (piedra-papel-tijera): ")
print(piedra_papel_tijera(jugador1, jugador2))