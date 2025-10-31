
nombres = []

def agregar_nombres():
    while True:
        nombre = input("Introduce un nombre (deja en blanco para finalizar): ")
        if nombre == "":  # Si el usuario no escribe nada, se termina el bucle
            break
        nombres.append(nombre)  # Agrega el nombre al final de la lista

    print("\nLista de nombres ingresados:")
    for n in nombres:
        print(n)