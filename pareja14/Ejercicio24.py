socios = {}
cont = 1000
morosos = 0
print("carge los datos de los socios del club 'CAVUL':")


for i in range (cont):
    dni = input("\ningrese el DNI del socio: ")
    if dni == "0":
        break
    
    nombre = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    edad = int(input("ingrese la edad: "))
    cuota = input("tiene la cuota al día? (si-no): ").lower()
    
    socios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "cuota_al_dia": cuota
    }
print("\nCantidad total de socios del club:", len(socios))

for socio in socios.values():
    if socio["cuota_al_dia"] == "no":
        morosos += 1
print("Cantidad de socios morosos:", morosos)

if "25123555" in socios:
    socio = socios["25123555"]
    print("se encontro un socio con el DNI: 25.123.555")
    print(f"nombre y apellido: {socio['nombre']} {socio['apellido']}")
else:
    print("no existe ningun socio con el DNI: 25.123.555.")

socios["40151724"] = {"nombre" : "esteban", "apellido" : "quito", "edad" : 17, "cuota_al_dia" : "si"}
print("nuevo socio agregado")

mayor_edad = 0
dni_mayor = ""
for dni in socios:
    if socios[dni]["edad"] > mayor_edad:
        mayor_edad = socios[dni]["edad"]
        dni_mayor = dni
print("el DNI del socio con mayor edad es: ", dni_mayor)

dni_baja = "15188125"
if dni_baja in socios:
    if socios[dni_baja]["cuota_al_dia"] == "si":
        del socios[dni_baja]
        print("socio eliminado")
    else:
        print("no se pudo dar de baja al socio: tiene la cuota pendiente")
else:
    print("no existe ningun socio con el DNI: 15.188.125")

dni_pago = "28731431"
if dni_pago in socios:
    socios[dni_pago]["cuota_al_dia"] = "si"
    print("cuota del mes pagada por: ", socios[dni_pago]["nombre"])
else:
    print("no existe ningun socio con el DNI: 28.731.431")