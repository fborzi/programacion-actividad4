def piedra_papel_tijera(uno, dos):
    uno = uno.lower()
    dos = dos.lower()

    if uno == dos:
        return 0
    elif (uno == "piedra" and dos == "tijera") or \
         (uno == "tijera" and dos == "papel") or \
         (uno == "papel" and dos == "piedra"):
        return 1
    else:
        return 2

print(piedra_papel_tijera("Piedra", "tijera"))  
print(piedra_papel_tijera("papel", "PIEDRA"))   
print(piedra_papel_tijera("tijera", "Papel"))   
print(piedra_papel_tijera("piedra", "Papel"))   
print(piedra_papel_tijera("tijera", "tijera"))  
