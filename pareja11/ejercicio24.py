socios = {}

dni = input("DNI (ingrese 0 para terminar): ")

while dni != "0":
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    cuota = input("¿Tiene la cuota al día? (Si/No): ").capitalize()

    socios[dni] = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Cuota": cuota
    }

    print("Socio cargado.\n")
    dni = input("DNI (ingrese 0 para terminar): ")

# a)
print(f"\na) Cantidad total de socios: {len(socios)}")

# b)
morosos = [s for s in socios.values() if s["Cuota"] == "No"]
print(f"b) Cantidad de socios morosos: {len(morosos)}")

# c)
dni_buscar = "25.123.555"
if dni_buscar in socios:
    s = socios[dni_buscar]
    print(f"c) El socio {dni_buscar} es {s['Nombre']} {s['Apellido']}")
else:
    print(f"c) No existe un socio con DNI {dni_buscar}")

# d)
nuevo_dni = "40.151.724"
socios[nuevo_dni] = {
    "Nombre": "Esteban",
    "Apellido": "Quito",
    "Edad": 17,
    "Cuota": "Si"
}
print(f"\nd) Se agregó el nuevo socio {nuevo_dni}: Esteban Quito, 17 años, cuota al día.")

# e)
dni_mayor = max(socios, key=lambda d: socios[d]["Edad"])
print(f"e) El socio de mayor edad es {socios[dni_mayor]['Nombre']} {socios[dni_mayor]['Apellido']} (DNI {dni_mayor})")

# f)
dni_baja = "15.188.125"
if dni_baja in socios:
    if socios[dni_baja]["Cuota"] == "Si":
        del socios[dni_baja]
        print(f"f) Socio {dni_baja} dado de baja correctamente.")
    else:
        print(f"f) No se puede dar de baja al socio {dni_baja} porque no tiene la cuota al día.")
else:
    print(f"f) No existe el socio con DNI {dni_baja}.")

# g)
dni_pago = "28.731.431"
if dni_pago in socios:
    socios[dni_pago]["Cuota"] = "Si"
    print(f"g) El socio {dni_pago} acaba de pagar su cuota.")
else:
    print(f"g) No existe el socio con DNI {dni_pago}.")
