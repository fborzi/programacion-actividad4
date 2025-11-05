def piedra_papel_tijera(uno, dos):
    
    uno = uno.lower()
    dos = dos.lower()

    
    if uno == dos:
        return 0

    if (uno == "piedra" and dos == "tijera") or \
       (uno == "tijera" and dos == "papel") or \
       (uno == "papel" and dos == "piedra"):
        return 1  # Gana el jugador 1
    else:
        return 2  # Gana el jugador 2
    print(piedra_papel_tijera("Piedra", "Tijera"))  # → 1
print(piedra_papel_tijera("papel", "PIEDRA"))   # → 1
print(piedra_papel_tijera("tijera", "papel"))   # → 1
print(piedra_papel_tijera("piedra", "papel"))   # → 2
print(piedra_papel_tijera("tijera", "tijera"))  # → 0

