'''Escribí la función indice_mayor(lista) que retorne el índice en el cual se encuentra el mayor número de la lista. Ejemplo: indice_mayor([6,1,7,19,2]) retornará 3.'''
from funciones import indice_mayor
lista=[]
n=int(input("Dame un numero distintro a 0: "))
while n!= 0:
    lista.append(n)
    n=int(input("Dame otro numero distintro a 0: "))
print(indice_mayor(lista))

