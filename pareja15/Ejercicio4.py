#Escribir un programa que pida al usuario el ingreso por teclado de una serie de nombres, terminando al leer un nombre en blanco. 
# A medida que se ingresan, agregar cada nombre al final de una lista. Al finalizar el ingreso se deben imprimir los elementos de dicha lista, iterando por ella.

nombres = []
nombre = input("Ingrese un nombre (deje en blanco para terminar): ")
while nombre != "":
    nombres.append(nombre)
    nombre = input("Ingrese un nombre (deje en blanco para terminar): ")

print("Nombres ingresados:")
for nombre in nombres:
    print(nombre)