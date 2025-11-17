'''Escribí un programa que almacene la información relacionada con pacientes: edad, sexo y si es diabético. Además, se registra el DNI de cada uno. Utilizá un diccionario para registrar los datos provistos en la tabla de más abajo, (deberás utilizar un contenedor para los valores). Se pide:'''

# Diccionario de pacientes: DNI → (edad, sexo, es_diabetico)
pacientes = {
    11412625: (60, 'Masculino', True),
    6409217: (65, 'Femenino', False),
    19172162: (45, 'Masculino', False),
    28141815: (34, 'Femenino', True),
    14972142: (58, 'Masculino', True),
    36843316: (23, 'Femenino', False)
}

# a. Cantidad de pacientes registrados
print(f"a. Total de pacientes registrados: {len(pacientes)}")

# b. Listado completo
print("\nb. Listado de pacientes:")
for dni, (edad, sexo, diabetico) in pacientes.items():
    print(f"  DNI: {dni} | Edad: {edad} | Sexo: {sexo} | Diabético: {'Sí' if diabetico else 'No'}")

# c. Incrementar edad de un paciente por DNI
dni_input = int(input("\nc. Ingresá el DNI del paciente para incrementar su edad: "))
if dni_input in pacientes:
    edad, sexo, diabetico = pacientes[dni_input]
    pacientes[dni_input] = (edad + 1, sexo, diabetico)
    print(f"  Edad actualizada: {pacientes[dni_input][0]}")
else:
    print("  DNI no encontrado.")

# d. Verificar si dos pacientes son diabéticos
print("\nd. Estado de diabetes:")
for dni_consulta in [14972142, 6409217]:
    if dni_consulta in pacientes:
        print(f"  DNI {dni_consulta}: {'Diabético' if pacientes[dni_consulta][2] else 'No diabético'}")
    else:
        print(f"  DNI {dni_consulta} no encontrado.")

# e. Edad promedio de pacientes con diabetes
diabeticos = [edad for edad, _, diab in pacientes.values() if diab]
if diabeticos:
    promedio = sum(diabeticos) / len(diabeticos)
    print(f"\ne. Edad promedio de pacientes con diabetes: {promedio:.2f}")
else:
    print("\ne. No hay pacientes con diabetes registrados.")

# f. ¿Hay algún paciente mayor de 80 años sin diabetes?
hay_mayor_sin_diabetes = any(edad > 80 and not diab for edad, _, diab in pacientes.values())
print("\nf. ¿Existe algún paciente mayor de 80 años sin diabetes?")
print("  Sí" if hay_mayor_sin_diabetes else "  No")