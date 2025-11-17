"""
EJERCICIO 14
Escribí la función dos_sumandos(lista, resultado) que, dada una lista 
compuesta por números y otro número cualquiera, retorne una nueva lista 
con dos elementos, que representarán índices de elementos de la lista 
original cuya suma da como resultado el número pasado por parámetro. 
De la lista original no se deberá utilizar el mismo número dos veces. 
Ejemplo: dos_sumandos([2, 7, 11, 15], 17) retornará [0, 3] 
ya que lista[0]+lista[3] = 17.

"""
from funciones import dos_sumando

entrada = input("Ingrese los números de la lista separados por espacios: ")

numeros = []
for numero_str in entrada.split():
    numeros.append(int(numero_str))

objetivo = int(input("Ingrese el número objetivo(la suma que busca): "))

indices = dos_sumando(numeros, objetivo)

print("Lista ingresada:", numeros)
print("Resultado buscado:", objetivo)
print("índices encontrados:", indices)

if len(indices) > 0:
    print("Verificación:", numeros[indices[0]], "+", numeros[indices[1]], "=", numeros[indices[0]] + numeros[indices[1]])
else:
    print("No se encontró ninguna combinación que sume", objetivo)