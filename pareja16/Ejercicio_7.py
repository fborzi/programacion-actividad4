
from funciones import dos_minimos

lista = []

cantidad = int(input("Ingresar la cantidad de elementos que va a contener la lista: "))

for i in range(cantidad):
    valor = float(input(f"Ingresar el elemento {i + 1}: "))
    lista.append(valor)

min1, min2 = dos_minimos(lista)

print("La lista creada es:  ", lista)
print("Primer valor mínimo: ", min1)
print("Segundo valor mínimo: ", min2)

