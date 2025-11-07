pacientes = {
    11412625: [60, "Masculino", True],
    6409217: [65, "Femenino", False],
    19172162: [45, "Masculino", False],
    28141815: [34, "Femenino", True],
    14972142: [58, "Masculino", True],
    36843316: [23, "Femenino", False]
}

# Informar cuántos pacientes hay registrados
print("Cantidad de pacientes registrados:", len(pacientes))

# 2Listar pacientes
print("\nListado de pacientes:")
for dni, (edad, sexo, diabetes) in pacientes.items():
    print(f"DNI: {dni} - Edad: {edad} - Sexo: {sexo} - Diabético: {'Si' if diabetes else 'No'}")

# Solicitar DNI e incrementar edad en 1
dni_ingresado = int(input("\nIngrese un DNI para aumentar su edad: "))

if dni_ingresado in pacientes:
    pacientes[dni_ingresado][0] += 1
    print("Edad actualizada.")
else:
    print("DNI no encontrado.")

# Indicar si sufren diabetes 14.972.142 y 6.409.217
print("\n¿El paciente 14972142 es diabético?",
      "Sí" if pacientes[14972142][2] else "No")

print("¿El paciente 6409217 es diabético?",
      "Sí" if pacientes[6409217][2] else "No")

# Edad promedio de los pacientes diabéticos
edades_diabeticos = [datos[0] for datos in pacientes.values() if datos[2]]

if edades_diabeticos:
    promedio = sum(edades_diabeticos) / len(edades_diabeticos)
    print(f"\nEdad promedio de pacientes diabéticos: {promedio:.2f}")
else:
    print("\nNo hay pacientes diabéticos")

# 6Indicar si existe algún paciente mayor de 80 sin diabetes
existe = any(edad > 80 and not diabetes for edad, _, diabetes in pacientes.values())
print("\n¿Hay paciente mayor de 80 años sin diabetes?",
      "Sí, existe al menos uno" if existe else "No, no existe ninguno")
