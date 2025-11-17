pacientes = {}

dni = int(input("Ingrese datos de pacientes (DNI 0 para terminar): "))
dni_str = str(dni)
while dni != 0 and len(dni_str) == 8 or len(dni_str) == 7:
    edad = int(input("Edad: "))
    sexo = input("Sexo (Masculino/Femenino): ").title()
    diabetico = input("¿Es diabetico? (Si/No): ").title()

    pacientes[dni] = [edad, sexo, diabetico]

    dni = int(input("Ingrese datos de pacientes (DNI 0 para terminar): "))

#A: informar cuantos pacientes hay registrados
print("=================================")
print("Cantida de pacientes registrados")
print("=================================")

cant_pacientes = len(pacientes)
print(cant_pacientes)

#B: listar todos los pacientes con su DNI y demas datos
print("=================================")
print("Lista de pacientes por DNI")
print("=================================")

for dni in pacientes:
    print(dni, edad,sexo,diabetico)

#C: solicitar un DNI e incrementar en 1 la edad
print("=================================")
print("Actualizar edad")
print("=================================")

dni_buscar = int(input("Ingrese su DNI: "))

if dni_buscar in pacientes:
    pacientes[dni_buscar][0] = pacientes[dni_buscar][0]+1
    print("Edad actualizada: ", {pacientes[dni_buscar][0]}, " Años")
else: 
    print("DNI no encontrado")

#D: indicar si los pacietes con DNI especifico sufren diabetes
print("=================================")
print("Consulta de diabetes: ")
print("=================================")
dni1 = 14972142
dni2 = 6409217

if dni1 in pacientes:
    if pacientes[dni1][2] == "Si":
        print("El paciente con DNI: ", dni1, " sufre diabetes")
    else:
        print("El paciente con DNI: ", dni1, " no sufre diabetes")
else:
    print("El DNI ", dni1, " no esta registrado")

if dni2 in pacientes:
    if pacientes[dni2][2] == "Si":
        print("El paciente con DNI: ", dni2, " sufre de diabetes")
    else:
        print("El paciente con DNI: ", dni1, " no sufre diabetes")
else: print("El DNI: ", dni2, " no esta registrado")

#E: calcular la edad promedio de pacientes con diabetes
print("=======================================")
print("Edad promedio de pacientes con diabetes")
print("=======================================")

suma_edades = 0
cantidad_diabeticos = 0

for dni in pacientes:
    if pacientes[dni][2] == "Si":
        suma_edades += pacientes[dni][0]
        cantidad_diabeticos += 1

if cantidad_diabeticos > 0:
    promedio = suma_edades / cantidad_diabeticos
    print("Edad promedio: ", promedio, " años")
else: 
    print("No hay pacientes diabeticos registados")

#F: Indicar si hay algun paciente mayor de 80 años sin diabetes 
print("=============================================")
print("¿Hay algun paciente mayor de 80 sin diabetes?")
print("=============================================")

encontrado = False 

for dni in pacientes:
    edad = pacientes[dni][0]
    diabetico = pacientes[dni][2]

    if edad > 80 and diabetico == "No":
        encontrado = True
        break
if encontrado:
    print("Si, hay al menos un paciente mayor de 80 años sin diabetes")
else: 
    print("No, no hay pacientes mayores de 80 años sin diabetes")
