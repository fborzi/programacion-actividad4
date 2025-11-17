def main():
    # Diccionario principal con los datos de los pacientes
    pacientes = {
        '11.412.625': {'edad': 60, 'sexo': 'Masculino', 'diabetico': 'Si'},
        '6.409.217': {'edad': 65, 'sexo': 'Femenino', 'diabetico': 'No'},
        '19.172.162': {'edad': 45, 'sexo': 'Masculino', 'diabetico': 'No'},
        '28.141.815': {'edad': 34, 'sexo': 'Femenino', 'diabetico': 'Si'},
        '14.972.142': {'edad': 58, 'sexo': 'Masculino', 'diabetico': 'Si'},
        '36.843.316': {'edad': 23, 'sexo': 'Femenino', 'diabetico': 'No'}
    }

    # A. Informar cuántos pacientes hay registrados
    print("A. Cantidad de pacientes registrados:", len(pacientes))

    # B. Listar todos los pacientes con su DNI y demás datos
    print("\nB. Listado de pacientes:")
    for dni, datos in pacientes.items():
        print(f"DNI: {dni}, Edad: {datos['edad']}, Sexo: {datos['sexo']}, Diabético: {datos['diabetico']}")

    # C. Solicitar al usuario un DNI e incrementar en 1 la edad del paciente correspondiente
    print("\nC. Actualización de edad:")
    dni_ingresado = input("Ingrese el DNI del paciente a actualizar: ")
    if dni_ingresado in pacientes:
        pacientes[dni_ingresado]['edad'] += 1
        print(f"Edad actualizada. Nueva edad: {pacientes[dni_ingresado]['edad']}")
    else:
        print("DNI no encontrado.")

    # D. Indicar si los pacientes con DNI 14.972.142 y 6.409.217 sufren de diabetes
    print("\nD. Condición de diabetes:")
    dni1 = '14.972.142'
    dni2 = '6.409.217'
    if dni1 in pacientes:
        print(f"Paciente {dni1}: {'Sí' if pacientes[dni1]['diabetico'] == 'Si' else 'No'} es diabético")
    if dni2 in pacientes:
        print(f"Paciente {dni2}: {'Sí' if pacientes[dni2]['diabetico'] == 'Si' else 'No'} es diabético")

    # E. Calcular la edad promedio de los pacientes con diabetes
    print("\nE. Edad promedio de pacientes diabéticos:")
    edades_diabeticos = [datos['edad'] for datos in pacientes.values() if datos['diabetico'] == 'Si']
    if edades_diabeticos:
        promedio = sum(edades_diabeticos) / len(edades_diabeticos)
        print(f"Edad promedio: {promedio:.2f} años")
    else:
        print("No hay pacientes diabéticos")

    # F. Indicar si existe algún paciente mayor de 80 años sin diabetes
    print("\nF. Verificación de paciente mayor de 80 años sin diabetes:")
    existe_mayor_sin_diabetes = any(
        datos['edad'] > 80 and datos['diabetico'] == 'No' 
        for datos in pacientes.values()
    )
    print("Sí existe" if existe_mayor_sin_diabetes else "No existe", "algún paciente mayor de 80 años sin diabetes")

if __name__ == "__main__":
    main()