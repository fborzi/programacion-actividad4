nombres = []

print("Ingrese nombres (presione ENTER para finalizar): ")

nombre = input("Nombre: ")

while nombre != "":
    nombres.append(nombre.upper())

    nombre = input("Nombre: ")

print('los nombres ingresados son: ')
for nombre in nombres:
    print(nombre)

