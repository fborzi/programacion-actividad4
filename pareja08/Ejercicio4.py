nombres = []

nombre = input("Ingrese un nombre. Presione enter para finalizar: ")
while nombre != "":
    nombres.append(nombre.lower())
    nombre = input("Ingrese un nombre. Presione enter para finalizar: ")
    
if len(nombres) == 0:
    print("No se han ingresado nombres.")
else:
    print("Los nombres ingresados son:")
    for nombre in nombres:
        print(f"● {nombre.title()}")