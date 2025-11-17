from Funciones import sumatoria_digitos
print("ingrese numeros enteros (dividos por ','): ")
lista = []
lista = input()
lista = lista.split(",")
suma = sumatoria_digitos(lista)
print(suma)