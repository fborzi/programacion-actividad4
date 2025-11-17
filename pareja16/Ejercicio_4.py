
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

