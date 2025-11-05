'''Escribí la función dos_minimos(lista) que reciba una lista de elementos comparables entre sí y devuelva los dos valores menores encontrados en la lista dada. Si la lista tuviera menos de dos elementos, retornar None por cada elemento faltante.
Ejemplos: dos_minimos([23, 456, 12, 16, -4, 56])retorna(-4, 12)
dos_minimos([4]) retorna (4, None)
dos_minimos([]) retorna (None, None)
'''
from funciones import dos_minimos
lista=[]
i=int(input("Dame un numero entero: "))
while i!=0:
    lista.append(i)
    i=int(input("Dame otro numero entero, distinto a 0: "))
print(dos_minimos(lista))