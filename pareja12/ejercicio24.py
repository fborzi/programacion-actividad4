socios = {}

print("Ingrese DNI. 0 para finalizar.")
dni = int(input("DNI: "))

while dni != 0:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad:"))
    cuota_al_dia = input("¿Tiene su cuota al día? (si/no): ").lower() == "si"

    socios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cuota_al_dia": cuota_al_dia
    }

    print("Socio registrado correctamente✅")
    dni = int(input("DNI: "))

# a) Informar la cantidad de socios del club.
cantidad_socios = len(socios)
print("1.Cantidad de socios del club:", cantidad_socios)

# b) Informar la cantidad de socios morosos
socios_morosos = 0
for dni in socios:
    if not socios[dni]["cuota_al_dia"]:
        socios_morosos += 1
print("2. Cantidad de socios morosos:", socios_morosos)

# c) Informar nombre y apellido del socio con DNI 25.123.555
dni_buscar = 25123555
if dni_buscar in socios:
    socio = socios[dni_buscar]
    print("3. Socio con DNI", dni_buscar, ":", socio['nombre'], socio['apellido'])
else:
    print("3. No existe un socio con DNI: ", dni_buscar)

# d) Dar de alta a un nuevo socio.
nuevo_dni = 40151724
socios[nuevo_dni] = {
    "nombre": "Esteban",
    "apellido": "Quito",
    "edad": 17,
    "cuota_al_dia": True
}
print("4. Alta de nuevo socio: Esteban Quito. DNI:", nuevo_dni)

# e) Informar el DNI del socio de mayor edad
if len(socios) > 0:
    dni_mayor_edad = None
    edad_maxima = 0

    for dni in socios:
        if socios[dni]["edad"] > edad_maxima:
            edad_maxima = socios[dni]["edad"]
            dni_mayor_edad = dni

    print("5. DNI del socio de mayor edad: ", dni_mayor_edad , (edad_maxima , 'años'))
else:
    print("5. NO hay socios registrados")

# f) Dar d baja al socio con DNI 15188125
dni_baja = 15188125
if dni_baja in socios:
    if socios[dni_baja]["cuota_al_dia"]:
        socio_eliminado = socios[dni_baja]
        del socios[dni_baja]
        print("6. Baja existosa:", socio_eliminado)
    else:
        print("6. No se puede dar de baja. El socio tiene cuota pendiente.")
else:
    print("6. No existe un socio con DNI ", dni_baja)

# g) Registrar pago de cuota del socio con DNI 28731431
dni_pago = 28731431
if dni_pago in socios:
    socios[dni_pago]["cuota_al_dia"] = True
    socio = socios[dni_pago]
    print(f"7. Pago resgistrado: {socio['nombre']} {socio['apellido']} - Cuota al día")
else:
    print(f"7. No existe un socio con DNI {dni_pago}")

print("Total de socios activos:", len(socios))