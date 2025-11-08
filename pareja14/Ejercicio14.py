from Funciones import dos_sumandos
lista = []
objetivo = []
lista = input("agrege numeros a la lista (separados por ','): ")
lista = [int(x) for x in lista.split(",")]
objetivo = int(input("ingrese el numero objetivo: "))
print("\nlas posiciones de los numeros clave son: ", dos_sumandos(lista, objetivo))