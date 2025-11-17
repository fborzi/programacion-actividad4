
from funciones import minimo_elemento

lista = []

cantidad = int(input("Ingresar la cantidad de elementos que va a contener la lista: "))

for i in range (cantidad):
    valor = float(input(f"Ingresar el elementos {i + 1}: "))
    lista.append(valor)

valor_minimo = minimo_elemento(lista)

print ("La lista creada es: ", lista)
print ("El minimo elemento de la lista ingresada es: ", valor_minimo)
