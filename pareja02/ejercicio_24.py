"""
EJERCICIO 24: Diccionario de pacientes
Almacenar información de pacientes (edad, sexo, diabético) por DNI.
"""

# Diccionario de pacientes (DNI: [edad, sexo, es_diabetico])
pacientes = {
    14972142: [45, 'F', True],
    6409217: [72, 'M', False],
    28765432: [38, 'F', True],
    35123456: [55, 'M', True],
    40987654: [29, 'F', False]
}

print("Sistema de Gestión de Pacientes")
print("="*60)

# a) Cantidad de pacientes registrados
print(f"\na) Cantidad de pacientes registrados: {len(pacientes)}")

# b) Listar todos los pacientes
print("\nb) Lista de pacientes:")
print("-"*60)
for dni, datos in pacientes.items():
    edad, sexo, diabetico = datos
    estado_diabetes = "Sí" if diabetico else "No"
    print(f"   DNI: {dni} | Edad: {edad} | Sexo: {sexo} | Diabético: {estado_diabetes}")

# c) Incrementar edad de un paciente
print("\nc) Incrementar edad del paciente:")
dni_buscar = int(input("   Ingrese DNI del paciente: "))
if dni_buscar in pacientes:
    edad_anterior = pacientes[dni_buscar][0]
    pacientes[dni_buscar][0] += 1
    print(f"   Edad actualizada: {edad_anterior} → {pacientes[dni_buscar][0]}")
else:
    print(f"   No se encontró paciente con DNI {dni_buscar}")

# d) Verificar diabetes de pacientes específicos
print("\nd) Verificar diabetes:")
dni1 = 14972142
dni2 = 6409217
print(f"   DNI {dni1} sufre de diabetes: {pacientes[dni1][2]}")
print(f"   DNI {dni2} sufre de diabetes: {pacientes[dni2][2]}")

# e) Edad promedio de pacientes con diabetes
print("\ne) Edad promedio de pacientes con diabetes:")
edades_diabeticos = [datos[0] for datos in pacientes.values() if datos[2]]
if edades_diabeticos:
    promedio = sum(edades_diabeticos) / len(edades_diabeticos)
    print(f"   Promedio: {promedio:.1f} años")
    print(f"   (Basado en {len(edades_diabeticos)} pacientes diabéticos)")
else:
    print("   No hay pacientes diabéticos registrados")

# f) Verificar si existe paciente >80 años sin diabetes
print("\nf) ¿Existe algún paciente mayor de 80 años sin diabetes?")
existe = False
for datos in pacientes.values():
    edad, sexo, diabetico = datos
    if edad > 80 and not diabetico:
        existe = True
        break

if existe:
    print("   SÍ, existe al menos un paciente mayor de 80 años sin diabetes")
else:
    print("   NO, no existe ningún paciente mayor de 80 años sin diabetes")
