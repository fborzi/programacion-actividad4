"""Escribir un programa que pida al usuario 
el ingreso por teclado de una serie de nombres, 
terminando al leer un nombre en blanco. 
A medida que se ingresan, agregar cada nombre al 
final de una lista. 
Al finalizar el ingreso se deben imprimir los 
elementos de dicha lista, iterando por ella."""

nombres = []

print("Ingrese nombres (presione ENTER para finalizar): ")

nombre = input("Nombre: ")

while nombre != "":
    nombres.append(nombre)

    nombre = input("Nombre: ")

print("Nombres ingresados: ")
for nombre in nombres:
    print(nombre)