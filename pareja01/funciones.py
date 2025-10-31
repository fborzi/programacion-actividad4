def dos_minimos(lista):
    largo = len(lista)
    if largo < 2:
        print("Primer valor menor: ", lista[0] if largo == 1 else "NONE", 
              ". Segundo valor menor: NONE")
        return (None,"NONE", None,"NONE")
    elif largo == 1:
        return (lista[0], None)
    
    min1 = float('inf')
    min2 = float('inf')
    
    for num in lista:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num
            
    if min2 == float('inf'):
        min2 = None
    print("Primer valor menor: ", min1, ". Segundo valor menor: ", min2)
    return (min1, min2)

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