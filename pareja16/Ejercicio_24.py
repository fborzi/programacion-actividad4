
# carga de socios
socios = {}

dni = input("Ingresar DNI (0 para terminar): ")

while dni != "0":
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    cuota = input("Cuota al dia? (s/n): ")

    socios[dni] = {
        "apellido": apellido,
        "nombre": nombre,
        "edad": edad,
        "cuota_al_dia": (cuota.lower() == "s")
    }

    dni = input("Ingresar DNI (0 para terminar): ")


# a) cantidad de socios
print("Cantidad de socios:", len(socios))

# b) cantidad de morosos
morosos = 0
for datos in socios.values():
    if not datos["cuota_al_dia"]:
        morosos += 1
print("Cantidad de socios morosos:", morosos)

# c) buscar socio 25123555
dni_buscar = "25123555"
if dni_buscar in socios:
    print("Socio", dni_buscar, ":", socios[dni_buscar]["nombre"], socios[dni_buscar]["apellido"])
else:
    print("No existe socio con DNI", dni_buscar)

# d) alta de nuevo socio
socios["40151724"] = {
    "apellido": "Quito",
    "nombre": "Esteban",
    "edad": 17,
    "cuota_al_dia": True
}

# e) socio de mayor edad
mayor_dni = ""
mayor_edad = -1
for dni, datos in socios.items():
    if datos["edad"] > mayor_edad:
        mayor_edad = datos["edad"]
        mayor_dni = dni
print("Socio de mayor edad (DNI):", mayor_dni)

# f) baja del socio 15188125 si cuota al día
dni_baja = "15188125"
if dni_baja in socios:
    if socios[dni_baja]["cuota_al_dia"]:
        del socios[dni_baja]
        print("Socio", dni_baja, "eliminado")
    else:
        print("No se puede eliminar al socio", dni_baja, "porque está moroso")
else:
    print("No existe socio con DNI", dni_baja)

# g) registrar pago de cuota para 28731431
dni_pago = "28731431"
if dni_pago in socios:
    socios[dni_pago]["cuota_al_dia"] = True
    print("Se registró el pago del socio", dni_pago)
else:
    print("No existe socio con DNI", dni_pago)

