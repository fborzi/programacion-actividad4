pacientes = {
    "11.412.625": {"Edad": 60, "Sexo": "Masculino", "Diabetico": "Si"},
    "6.409.217": {"Edad": 65, "Sexo": "Femenino", "Diabetico": "No"},
    "19.172.162": {"Edad": 45, "Sexo": "Masculino", "Diabetico": "No"},
    "28.141.815": {"Edad": 34, "Sexo": "Femenino", "Diabetico": "Si"},
    "14.972.142": {"Edad": 58, "Sexo": "Masculino", "Diabetico": "Si"},
    "36.843.316": {"Edad": 23, "Sexo": "Femenino", "Diabetico": "No"}
}

# a)
print("a) Cantidad de pacientes registrados:", len(pacientes))

# b) 
print("\nb) Lista de pacientes:")
for dni, datos in pacientes.items():
    print(f"  DNI: {dni} - Edad: {datos['Edad']} - Sexo: {datos['Sexo']} - Diabético: {datos['Diabetico']}")

# c) 
dni_ingresado = input("\nc) Ingresá un DNI para aumentar su edad en 1: ")
if dni_ingresado in pacientes:
    pacientes[dni_ingresado]["Edad"] += 1
    print(f"Edad actualizada de {dni_ingresado}: {pacientes[dni_ingresado]['Edad']}")
else:
    print("DNI no encontrado.")

# d) 
print("\nd) Estado de diabetes:")
for dni in ["14.972.142", "6.409.217"]:
    if dni in pacientes:
        print(f"  Paciente {dni}: Diabético = {pacientes[dni]['Diabetico']}")

# e) 
edades_diabeticos = [datos["Edad"] for datos in pacientes.values() if datos["Diabetico"] == "Si"]
if edades_diabeticos:
    promedio = sum(edades_diabeticos) / len(edades_diabeticos)
    print(f"\ne) Edad promedio de pacientes con diabetes: {promedio:.2f}")
else:
    print("\ne) No hay pacientes con diabetes.")

# f) 
hay_mayor_80_sin_diabetes = any(datos["Edad"] > 80 and datos["Diabetico"] == "No" for datos in pacientes.values())
print("\nf) ¿Hay algún paciente mayor de 80 años sin diabetes?:", "Sí" if hay_mayor_80_sin_diabetes else "No")
