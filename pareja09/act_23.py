# Diccionario principal
# Cada DNI tiene una lista con [edad, sexo, diabetico]
pacientes = {
    11412625: [60, "M", True],
    6409217: [65, "F", False],
    19172162: [45, "M", False],
    28141815: [34, "F", True],
    14972142: [58, "M", True],
    36843316: [23, "F", False]
}

# 1) Cantidad de pacientes
print("---caso 1---")
print("Cantidad de pacientes:", len(pacientes))
print()

# 2) Listar todos los pacientes
print("---caso 2---")
print("Listado de pacientes:")
for dni, datos in pacientes.items():
    print("DNI:", dni, "| Edad:", datos[0], "| Sexo:", datos[1], "| Diabético:", datos[2])
print()

# 3) Pedir DNI al usuario e incrementar su edad
print("---caso 3---")
dni_buscar = int(input("Ingrese un DNI para aumentar la edad: "))

if dni_buscar in pacientes:
    pacientes[dni_buscar][0] += 1
    print("Edad actualizada:", pacientes[dni_buscar][0])
else:
    print("Ese DNI no existe.")
print()

# 4) Indicar si estos pacientes sufren de diabetes
print("---caso 4---")
print("¿14972142 es diabético?:", pacientes[14972142][2])
print("¿6409217 es diabético?:", pacientes[6409217][2])
print()

# 5) Edad promedio de pacientes diabéticos
print("---caso 5---")
suma_edades = 0
contador = 0

for datos in pacientes.values():
    if datos[2] == True:
        suma_edades += datos[0]
        contador += 1

if contador > 0:
    promedio = suma_edades / contador
    print("Edad promedio de diabéticos:", promedio)
else:
    print("No hay pacientes diabéticos.")
print()

# 6) ¿Hay paciente mayor a 80 sin diabetes?
hay = False

for datos in pacientes.values():
    if datos[0] > 80 and datos[2] == False:
        hay = True

if hay:
    print("Hay al menos un paciente mayor de 80 sin diabetes.")
else:
    print("No hay pacientes mayores de 80 sin diabetes.")
