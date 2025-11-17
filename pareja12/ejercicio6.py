"""
Ejercicio6
Implementar la función minimo_elemento(lista) que recibe como parámetro una lista de elementos 
comparables entre sí y devuelve el mínimo valor encontrado en dicha lista o None si la lista fuera 
vacía.

Ejemplos:minimo_elemento([4, 8, 15, 16, 23, 42])
 retorna 4
minimo_elemento("PYTHON") retorna 'H'

"""

from funciones import minimo_elemento

#Lista de numeros
resultado1 = minimo_elemento([4, 8, 15, 16, 23, 42])
print("minimo_elemento([4, 8, 15, 16, 23, 42])=", resultado1)

#Cadena de caracteres
resultado2 = minimo_elemento("PYTHON")
print("minimo_elemento('PYTHON')=", resultado2)

#Lista vacia
resultado3 = minimo_elemento([])
print("minimo_elemento([])= ", resultado3)

#Lista con números negativos
resultado4 = minimo_elemento([-5, 3, -10, 8])
print("minimo_elemento([-5, 3, -10, 8])", resultado4)