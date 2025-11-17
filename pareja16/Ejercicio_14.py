
from funciones import dos_sumandos

cantidad = int(input("Cantidad de numeros a ingresar:  "))
lista_numeros = []

for i in range(cantidad):
    numero = int(input(f"Ingresar el número {i+1}: "))
    lista_numeros.append(numero)

resultado = int(input("Ingresar el número resultado a buscar: "))

indices = dos_sumandos(lista_numeros, resultado)

print("Lista ingresada: ", lista_numeros)

if indices is not None:
    print("Los índices de los elementos cuya suma da ", resultado, " son: ", indices)
    print("Los elementos son: ", lista_numeros[indices[0]], " y ", lista_numeros[indices[1]])
else:
    print("No se encontraron dos números que sumen ", resultado)
