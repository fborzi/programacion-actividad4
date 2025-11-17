def piedra_papel_tijera(uno,dos):
    #determina el ganador del juego

    #ignorar mayusculas/minusculas
    uno = uno.lower()
    dos = dos.lower()

    #en caso de que haya empate
    if uno == dos:
        return 0

    #condiciones en las que gana el jugador 
    if (uno == "piedra" and dos == "tijera") or\
        (uno == "tijera" and dos == "papel") or\
        (uno == "papel" and dos == "piedra"):
        return 1
    else:
        return 2
#ejemplos
print(piedra_papel_tijera("piedra", "tijera")) 
print(piedra_papel_tijera("Papel", "TIJERA"))
print(piedra_papel_tijera("tijera", "tijera"))