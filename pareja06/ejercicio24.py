"""
Ejercicio 24:
Sistema de gestión de socios del club CAVUL
"""

print("=== CLUB CAVUL - SISTEMA DE SOCIOS ===")
print()

# Diccionario para almacenar socios
# Clave: DNI, Valor: diccionario con datos del socio
socios = {}

# Ingreso de datos de socios
print("Ingrese los datos de los socios (DNI '0' para finalizar)")
print()

while True:
    dni = input("DNI: ")
    
    # Si ingresa '0', terminamos la carga
    if dni == "0":
        break
    
    # Solicitamos los demás datos
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    cuota_al_dia = input("¿Tiene la cuota al día? (si/no): ").lower() == "si"
    
    # Almacenamos el socio en el diccionario
    socios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cuota_al_dia": cuota_al_dia
    }
    
    print(f"✓ Socio {nombre} {apellido} registrado")
    print()

# === CONSULTAS E INFORMES ===
print()
print("=" * 60)
print("INFORMES Y OPERACIONES")
print("=" * 60)
print()

# a) Informar la cantidad de socios del club
print("a) Cantidad de socios del club:")
print(f"   Total de socios: {len(socios)}")
print()

# b) Informar la cantidad de socios morosos
print("b) Cantidad de socios morosos:")
morosos = 0
for dni, datos in socios.items():
    if not datos["cuota_al_dia"]:
        morosos += 1
print(f"   Socios morosos: {morosos}")
print()

# c) Informar el nombre y apellido del socio cuyo DNI es 25.123.555
print("c) Buscar socio con DNI 25.123.555:")
dni_buscado = "25123555"
if dni_buscado in socios:
    socio = socios[dni_buscado]
    print(f"   Socio encontrado: {socio['nombre']} {socio['apellido']}")
else:
    print(f"   No existe un socio con DNI {dni_buscado}")
print()

# d) Dar de alta a un nuevo socio
print("d) Alta de nuevo socio:")
socios["40151724"] = {
    "nombre": "Esteban",
    "apellido": "Gonzalez",
    "edad": 17,
    "cuota_al_dia": True
}
print(f"   ✓ Socio Esteban Gonzalez dado de alta (DNI: 40.151.724)")
print()

# e) Informar el DNI del socio de mayor edad
print("e) Socio de mayor edad:")
if len(socios) > 0:
    dni_mayor = None
    edad_maxima = -1
    
    for dni, datos in socios.items():
        if datos["edad"] > edad_maxima:
            edad_maxima = datos["edad"]
            dni_mayor = dni
    
    if dni_mayor:
        socio_mayor = socios[dni_mayor]
        print(f"   DNI: {dni_mayor}")
        print(f"   Nombre: {socio_mayor['nombre']} {socio_mayor['apellido']}")
        print(f"   Edad: {socio_mayor['edad']} años")
else:
    print("   No hay socios registrados")
print()

# f) Dar de baja al socio con DNI 15.188.125
print("f) Baja del socio con DNI 15.188.125:")
dni_baja = "15188125"
if dni_baja in socios:
    socio_baja = socios[dni_baja]
    if socio_baja["cuota_al_dia"]:
        del socios[dni_baja]
        print(f"   ✓ Socio {socio_baja['nombre']} {socio_baja['apellido']} dado de baja")
    else:
        print(f"   ✗ No se puede dar de baja. El socio está moroso")
else:
    print(f"   ✗ No existe un socio con DNI {dni_baja}")
print()

# g) Registrar pago de cuota del socio con DNI 28.731.431
print("g) Registrar pago de cuota del socio con DNI 28.731.431:")
dni_pago = "28731431"
if dni_pago in socios:
    socios[dni_pago]["cuota_al_dia"] = True
    socio_pago = socios[dni_pago]
    print(f"   ✓ Pago registrado para {socio_pago['nombre']} {socio_pago['apellido']}")
else:
    print(f"   ✗ No existe un socio con DNI {dni_pago}")
print()

# === LISTADO FINAL DE SOCIOS ===
print("=" * 60)
print("LISTADO FINAL DE SOCIOS")
print("=" * 60)
print()

if len(socios) > 0:
    for dni, datos in socios.items():
        estado = "✓ Al día" if datos["cuota_al_dia"] else "✗ Moroso"
        print(f"DNI: {dni}")
        print(f"   Nombre: {datos['nombre']} {datos['apellido']}")
        print(f"   Edad: {datos['edad']} años")
        print(f"   Estado: {estado}")
        print()
else:
    print("No hay socios registrados")
    print()

print(f"Total de socios: {len(socios)}")