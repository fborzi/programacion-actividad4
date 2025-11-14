#Ejercicio22 
socios = {}
dni = input("Ingrese el DNI del socio (0 para terminar): ")
while dni != "0":
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    cuota = input("¿Tiene la cuota al día? (s/n): ").lower() == "s"

    socios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cuota_al_dia": cuota
    }

    dni = input("Ingrese el DNI del socio (0 para terminar): ")

# a) Cantidad de socios
print("La cantidad total de socios es:", len(socios))

# b) Cantidad de socios morosos
morosos = [dni for dni, datos in socios.items() if not datos["cuota_al_dia"]]
print("La cantidad de socios morosos es:", len(morosos))

# c) Buscar socio con DNI 25.123.555
dni_buscar = "25123555"
if dni_buscar in socios:
    socio = socios[dni_buscar]
    print("El socio con DNI", dni_buscar, "es:", socio["nombre"], socio["apellido"])
else:
    print("No existe un socio con el DNI", dni_buscar)

# d) Dar de alta a un nuevo socio
socios["40151724"] = {
    "nombre": "Esteban",
    "apellido": "Quito",
    "edad": 17,
    "cuota_al_dia": True
}
print("Se dio de alta al nuevo socio Esteban Quito.")

# e) Informar el documento del socio de mayor edad
mayor_edad = max(socios.items(), key=lambda x: x[1]["edad"])
print("El socio de mayor edad tiene DNI:", mayor_edad[0])

# f) Dar de baja al socio con DNI 15.188.125 si tiene la cuota al día
dni_baja = "15188125"
if dni_baja in socios:
    if socios[dni_baja]["cuota_al_dia"]:
        del socios[dni_baja]
        print("El socio con DNI", dni_baja, "fue dado de baja.")
    else:
        print("El socio con DNI", dni_baja, "no tiene la cuota al día. No puede darse de baja.")
else:
    print("No existe un socio con el DNI", dni_baja)

# g) Registrar pago del socio 28.731.431
dni_pago = "28731431"
if dni_pago in socios:
    socios[dni_pago]["cuota_al_dia"] = True
    print("El socio con DNI", dni_pago, "ha pagado su cuota.")
else:
    print("No existe un socio con el DNI", dni_pago)

# Mostrar el diccionario final
print("Diccionario final de socios:", socios)