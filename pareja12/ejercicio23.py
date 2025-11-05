pacientes = {}

dni = int(input("Ingrese datos de pacientes (DNI 0 para terminar): "))

while dni != 0 and len(dni) == 8:
    edad = int(input("Edad: ")).lower()
    sexo = input("Sexo (Masculino/Femenino): ").lower()
    diabetico = input("¿Es diabetico? (Si/No): ").lower()

    pacientes[dni] = [edad, sexo, diabetico]

    dni = int(input("Ingrese datos de pacientes (DNI 0 para terminar): "))

#A: informar cuantos pacientes hay registrados
cant_pacientes = len(pacientes)
print("La cantidad de pacientes registrados es: ", cant_pacientes)

#B: listar todos los pacientes con su DNI y demas datos

for dni in pacientes:
    print(dni, edad,sexo,diabetico)

#C: solicitar un DNI e incrementar en 1 la edad
dni_buscar = int(input("Ingrese su DNI: "))

if dni_buscar in pacientes:
    pacientes[dni_buscar][0] = pacientes[dni_buscar][0]+1
    print("Edad actualizada: ", {pacientes[dni_buscar][0]}, " Años")
else: 
    print("DNI no encontrado")

#D: indicar si los pacietes con DNI especifico sufren diabetes
print("Consulta de diabetes: ")
dni1 = 14972142
dni2 = 06409217

if dni1 in pacientes:
    if pacientes[dni1][2] == "si":
        print("El paciente con DNI: ", dni1, " sufre diabetes")
    else:
        print("El paciente con DNI: ", dni1, " no sufre diabetes")
else:
    print("El DNI ", dni1, " no esta registrado")
