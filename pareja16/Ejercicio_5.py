
# Crear una lista vacía
nombres = []

# Pedir el primer nombre antes del bucle

nombre = input("Ingresá un nombre (o dejá en blanco para terminar): ")

# Repetir mientras el nombre no esté en blanco

while nombre != "":
    nombres.append(nombre)
    nombre = input("Ingresá un nombre (o dejá en blanco para terminar): ")

# Mostrar los nombres ingresados

print("Lista de nombres ingresados:")

for n in nombres:

    print(n)

# Crear una lista vacía para los nombres en mayúsculas

nombres_mayusculas = []

# Recorrer la lista original y convertir cada nombre a mayúsculas

for n in nombres:
    nombres_mayusculas.append(n.upper())

# Mostrar la lista en mayúsculas

print("Nombres en mayúsculas:")

for n in nombres_mayusculas:
    print(n)