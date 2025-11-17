nombres = [] #Lista vacía para almacenar los nombres

while True:
    nombre = input("Ingresa un nombre (dejar en blanco para finalizar): ")
    if nombre == "":
        break
    nombres.append(nombre) #Estructura de control para ingresar los nombres y finalizar en el caso de no ingresar nada

print("\nLista de nombres ingresados:")
for nombre in nombres:
    print(nombre) #Imprime los nombres ingresados 