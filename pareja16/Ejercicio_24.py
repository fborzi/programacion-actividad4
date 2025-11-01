# Programa: Gestión de socios del Club CAVUL

# Estructura: diccionario
# Clave: DNI / Valor: [nombre, apellido, edad, cuota_al_dia]

socios = {}

# --- Carga de datos ---
while True:
    dni = int(input("Ingrese el DNI del socio (0 para finalizar): "))
    if dni == 0:
        break
    
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    cuota = input("¿Tiene la cuota al día? (s/n): ").lower() == 's'
    
    socios[dni] = [nombre, apellido, edad, cuota]
    print("Socio cargado correctamente.\n")

# --- 1. Informar la cantidad de socios ---
print(f"\nCantidad total de socios: {len(socios)}")

# --- 2. Informar la cantidad de socios morosos ---
morosos = sum(1 for datos in socios.values() if not datos[3])
print(f"Cantidad de socios morosos: {morosos}")

# --- 3. Buscar socio por DNI 25.123.555 ---
dni_buscar = 25123555
if dni_buscar in socios:
    nombre, apellido, _, _ = socios[dni_buscar]
    print(f"Socio encontrado ({dni_buscar}): {nombre} {apellido}")
else:
    print(f"No existe un socio con DNI {dni_buscar}.")

# --- 4. Dar de alta nuevo socio ---
nuevo_dni = 40151724
socios[nuevo_dni] = ['Esteban', 'Quito', 17, True]
print(f"Nuevo socio agregado: Esteban Quito (DNI: {nuevo_dni})")

# --- 5. Informar DNI del socio de mayor edad ---
dni_mayor = max(socios, key=lambda dni: socios[dni][2])
print(f"El socio de mayor edad tiene DNI: {dni_mayor} ({socios[dni_mayor][0]} {socios[dni_mayor][1]})")

# --- 6. Dar de baja al socio con DNI 15.188.125 ---
dni_baja = 15188125
if dni_baja in socios:
    if socios[dni_baja][3]:  # cuota al día
        del socios[dni_baja]
        print(f"Socio con DNI {dni_baja} dado de baja correctamente.")
    else:
        print(f"No se puede dar de baja al socio {dni_baja} porque no tiene la cuota al día.")
else:
    print(f"No existe un socio con DNI {dni_baja}.")

# --- 7. Registrar pago de cuota del socio 28.731.431 ---
dni_pago = 28731431
if dni_pago in socios:
    socios[dni_pago][3] = True
    print(f"Socio {dni_pago} ahora tiene la cuota al día.")
else:
    print(f"No existe un socio con DNI {dni_pago}.")

# --- Resumen final (opcional) ---
print("\nListado actualizado de socios:")
for dni, datos in socios.items():
    nombre, apellido, edad, cuota = datos
    print(f"DNI: {dni} | {nombre} {apellido}, {edad} años, Cuota al día: {'Sí' if cuota else 'No'}")
