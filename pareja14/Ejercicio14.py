from Funciones import dos_sumandos
lista = []
objetivo = []
print("agrege numeros a la lista (separados por ','): ")
lista = input()
lista = lista.split(",")
objetivo = input("ingrese el numero objetivo: ")
print("\nlas posiciones de los numeros clave son: ", dos_sumandos(lista, objetivo))
print(lista)
print(objetivo)