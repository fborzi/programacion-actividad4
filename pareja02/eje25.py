#EJE25

print("Sistema de Gestión de Socios - Club CAVUL")
print("="*60)

# Diccionario de socios (DNI: [nombre, apellido, edad, cuota_al_dia])
socios = {}

# Ingreso de datos (simulado con datos de ejemplo para demostración)
print("\nIngreso de datos de socios:")
print("(Ingrese DNI '0' para finalizar)")
print("-"*60)

# Datos de ejemplo para demostración
datos_ejemplo = [
    (25123555, "Juan", "Pérez", 35, True),
    (15188125, "María", "González", 42, False),
    (28731431, "Carlos", "Rodríguez", 28, False),
    (32456789, "Ana", "Martínez", 31, True),
]

# Cargar datos de ejemplo
for dni, nombre, apellido, edad, cuota in datos_ejemplo:
    socios[dni] = [nombre, apellido, edad, cuota]
    print(f"Socio agregado: {nombre} {apellido} (DNI: {dni})")

print("\n" + "="*60)

# a) Cantidad de socios
print(f"\na) Cantidad de socios del club: {len(socios)}")

# b) Cantidad de socios morosos
morosos = sum(1 for datos in socios.values() if not datos[3])
print(f"\nb) Cantidad de socios morosos: {morosos}")

# c) Buscar socio por DNI
print("\nc) Buscar socio con DNI 25.123.555:")
dni_buscar = 25123555
if dni_buscar in socios:
    nombre, apellido, edad, cuota = socios[dni_buscar]
    print(f"   Socio encontrado: {nombre} {apellido}")
else:
    print(f"   No existe un socio con DNI {dni_buscar}")

# d) Dar de alta nuevo socio
print("\nd) Dar de alta nuevo socio:")
nuevo_dni = 40151724
socios[nuevo_dni] = ["Esteban", "Quito", 17, True]
print(f"   Socio agregado: {socios[nuevo_dni][0]} {socios[nuevo_dni][1]}")
print(f"   DNI: {nuevo_dni}, Edad: {socios[nuevo_dni][2]}, Cuota al día: Sí")

# e) Socio de mayor edad
print("\ne) Socio de mayor edad:")
dni_mayor = max(socios.keys(), key=lambda dni: socios[dni][2])
print(f"   DNI: {dni_mayor}")
print(f"   Nombre: {socios[dni_mayor][0]} {socios[dni_mayor][1]}")
print(f"   Edad: {socios[dni_mayor][2]} años")

# f) Dar de baja socio
print("\nf) Dar de baja socio con DNI 15.188.125:")
dni_baja = 15188125
if dni_baja in socios:
    nombre, apellido, edad, cuota = socios[dni_baja]
    if cuota:
        del socios[dni_baja]
        print(f"   Socio {nombre} {apellido} dado de baja exitosamente")
    else:
        print(f"   ERROR: El socio {nombre} {apellido} no tiene la cuota al día")
        print("   No se puede dar de baja")
else:
    print(f"   ERROR: No existe un socio con DNI {dni_baja}")

# g) Registrar pago de cuota
print("\ng) Registrar pago de cuota del socio con DNI 28.731.431:")
dni_pago = 28731431
if dni_pago in socios:
    nombre, apellido, edad, cuota = socios[dni_pago]
    print(f"   Estado anterior: {'Al día' if cuota else 'Moroso'}")
    socios[dni_pago][3] = True
    print(f"   Estado actual: Al día")
    print(f"   Pago registrado para {nombre} {apellido}")
else:
    print(f"   ERROR: No existe un socio con DNI {dni_pago}")

# Mostrar lista final de socios
print("\n" + "="*60)
print("Lista final de socios:")
print("-"*60)
for dni, datos in socios.items():
    nombre, apellido, edad, cuota = datos
    estado = "✓ Al día" if cuota else "✗ Moroso"
    print(f"DNI: {dni} | {nombre} {apellido} | Edad: {edad} | {estado}")
