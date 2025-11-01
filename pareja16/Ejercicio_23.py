# Diccionario que almacena los datos de los pacientes
# Clave: DNI / Valor: (edad, sexo, es_diabético)
pacientes = {
    14972142: [65, 'F', True],
    6409217: [82, 'M', False],
    39874215: [40, 'F', True],
    27345190: [50, 'M', False],
    12345678: [77, 'M', True],
}

# 1. Informar cuántos pacientes hay registrados
print(f"Cantidad de pacientes registrados: {len(pacientes)}\n")

# 2. Listar todos los pacientes con su DNI y demás datos
print("Listado de pacientes:")
for dni, datos in pacientes.items():
    edad, sexo, diabetes = datos
    print(f"DNI: {dni} | Edad: {edad} | Sexo: {sexo} | Diabético: {'Sí' if diabetes else 'No'}")
print()

# 3. Solicitar al usuario un DNI e incrementar en 1 la edad del paciente correspondiente
dni_buscar = int(input("Ingrese el DNI de un paciente para incrementar su edad: "))
if dni_buscar in pacientes:
    pacientes[dni_buscar][0] += 1
    print(f"Edad actualizada. Nueva edad: {pacientes[dni_buscar][0]} años\n")
else:
    print("El DNI ingresado no está registrado.\n")

# 4. Indicar si los pacientes con DNI 14.972.142 y 6.409.217 sufren de diabetes
for dni in [14972142, 6409217]:
    if dni in pacientes:
        print(f"El paciente con DNI {dni} {'es diabético' if pacientes[dni][2] else 'no es diabético'}.")
    else:
        print(f"No se encontró al paciente con DNI {dni}.")
print()

# 5. Calcular la edad promedio de los pacientes con diabetes
diabeticos = [datos[0] for datos in pacientes.values() if datos[2]]
if diabeticos:
    promedio = sum(diabeticos) / len(diabeticos)
    print(f"Edad promedio de pacientes con diabetes: {promedio:.2f} años\n")
else:
    print("No hay pacientes con diabetes registrados.\n")

# 6. Indicar si existe algún paciente mayor de 80 años sin diabetes
hay_mayor_80_no_diabetico = any(edad > 80 and not diabetes for edad, _, diabetes in pacientes.values())
if hay_mayor_80_no_diabetico:
    print("Existe al menos un paciente mayor de 80 años sin diabetes.")
else:
    print("No hay pacientes mayores de 80 años sin diabetes.")
