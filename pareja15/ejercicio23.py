# Diccionario de pacientes

# Diccionario de pacientes DNI: edad, sexo, es_diabetico 
pacientes = {
    14972142: [45, 'M', True],
    6409217: [72, 'F', False],
    20456789: [38, 'M', True],
    33567890: [65, 'F', True],
    28123456: [52, 'M', False],
    35678901: [81, 'M', False]
}

# Informar cuántos pacientes hay registrados
print("\nh) Cantidad de pacientes registrados:")
cantidad_pacientes = len(pacientes)
print(f"Total de pacientes: {cantidad_pacientes}")

# Listar todos los pacientes con su DNI y demás datos
print("\ni) Lista de todos los pacientes:")
print(f"{'DNI':<12} {'Edad':<6} {'Sexo':<6} {'Diabético':<10}")
print("-" * 40)
for dni, datos in pacientes.items():
    edad, sexo, diabetico = datos
    diabetico_str = "Sí" if diabetico else "No"
    print(f"{dni:<12} {edad:<6} {sexo:<6} {diabetico_str:<10}")

# Solicitar un DNI e incrementar en 1 la edad
print("\nj) Incrementar edad de un paciente:")
try:
    dni_input = int(input("Ingrese el DNI del paciente: "))
    if dni_input in pacientes:
        pacientes[dni_input][0] += 1
        print(f"Edad incrementada. Nueva edad: {pacientes[dni_input][0]}")
    else:
        print("DNI no encontrado en el registro")
except ValueError:
    print("Error: Ingrese un DNI válido")

# Indicar si los pacientes con DNI específicos sufren diabetes
print("\nk) Verificar diabetes en pacientes específicos:")
dni1 = 14972142
dni2 = 6409217

if dni1 in pacientes:
    diabetico1 = pacientes[dni1][2]
    print(f"Paciente con DNI {dni1}: {'SÍ' if diabetico1 else 'NO'} sufre de diabetes")

if dni2 in pacientes:
    diabetico2 = pacientes[dni2][2]
    print(f"Paciente con DNI {dni2}: {'SÍ' if diabetico2 else 'NO'} sufre de diabetes")

# Calcular edad promedio de pacientes con diabetes
print("\nl) Edad promedio de pacientes con diabetes:")
edades_diabeticos = [datos[0] for datos in pacientes.values() if datos[2]]

if edades_diabeticos:
    promedio_edad = sum(edades_diabeticos) / len(edades_diabeticos)
    print(f"Edad promedio: {promedio_edad:.2f} años")
else:
    print("No hay pacientes diabéticos registrados")

# Indicar si existe algún paciente mayor de 80 años sin diabetes
print("\nm) ¿Existe algún paciente mayor de 80 años sin diabetes?")
existe = any(datos[0] > 80 and not datos[2] for datos in pacientes.values())

if existe:
    print("SÍ existe al menos un paciente mayor de 80 años sin diabetes")
else:
    print("NO existe ningún paciente mayor de 80 años sin diabetes")