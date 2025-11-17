"""
EJERCICIO 16
Creá el conjunto numeros con los números del uno al diez. 
Luego, añadí el once y el doce. 
Actualizá la estructura incorporando los números del 30 al 35. 
Pensá en alguna forma de no tener que incorporarlos de a uno. 
Finalmente, agregá también los números 232 y -264.
Informar, de ser posible, el primer y el último número almacenado.
Informar si el 7 y el 20 pertenecen al conjunto.
Informar cuántos elementos hay almacenados.
"""

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Conjunto inicial: ", numeros)
print()

numeros.add(11)
numeros.add(12)
print("Añadimos los números 11 y 12", numeros)
print()

#Actualizamos incorporando los numeros del 30 al 35.
numeros.update(range(30, 36))
print("Añadimos los numeros del 30 al 35", numeros)
print()

#Agregamos los numeros 232 y -264
numeros.add(232)
numeros.add(-264)
print("Añadimos los numero 232 y -264", numeros)

#1. Informar el primero y ultimo número almacenado.
numeros_ordenados = sorted(numeros)
print("1. Primer número almacenado:", numeros_ordenados[0])
print("   Último número almacenado:", numeros_ordenados[-1])
print()

#2. Verificar si el 7 y el 20 pertenecen al conjunto
print("2. ¿El 7 pertenece al conjunto?", 7 in numeros)
print("   ¿El 20 pertenece al conjunto?", 20 in numeros)
print()

#3.Informar cuantos elementos hay almacenados
print("3. Cantidad de elementos almacenados", len(numeros))