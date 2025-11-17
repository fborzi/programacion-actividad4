"""
EJERCICIO 12
Escribí la función sumatoria_digitos(lista) que, dada una lista de números 
enteros positivos retornará una lista con la suma de los dígitos de cada 
uno de los números. 

Ejemplo: sumatoria_digitos([154, 27890, 111, 43]) retornará [10, 26, 3, 7]. 
Para lograr su cometido, esta función deberá valerse de otra, llamada 
suma_digitos(n) que, dado un número entero n retornará la suma de sus 
dígitos.

"""
from funciones import suma_digitos, sumatoria_digitos

cantidad = int(input("¿Cuántos números desea ingresar?: "))

numeros = []

for i in range(cantidad):
    numero = int(input("Ingrese el número " + str(i+1) + ": "))
    numeros.append(numero)

resultado = sumatoria_digitos(numeros)

print()
print("Lista ingresada:", numeros)
print("Suma de dígitos:", resultado)
