socios = []

dni = int(input("Ingrese el DNI del socio. Ingrese 0 para finalizar: "))
while dni != 0:
    socio = {}
    socio["dni"] = dni
    socio["nombre"] = input("Ingrese el nombre del socio: ")
    socio["apellido"] = input("Ingrese el apellido del socio: ")
    socio["edad"] = int(input("Ingrese la edad del socio: "))
    cuota = input("Ingrese si el socio tiene su cuota al dia [S/N]: ")
    socio["cuota"] = cuota.upper() == "S"
    socios.append(socio)
    dni = int(input("Ingrese el DNI del socio. Ingrese 0 para finalizar: "))
        

# a)
print(f"a) Cantidad de socios: {len(socios)}")

# b)
morosos = 0
for s in socios:
    if not s["cuota"]:
        morosos += 1
print(f"b) Socios morosos: {morosos}")

# c)
print("c)")
existe = False
for s in socios:
    if s["dni"] == 25123555:
        existe = True

if existe:
    print(f"Nombre de socio: {s['nombre']}\nApellido del socio: {s['apellido']}")
else:
    print("El socio con DNI 25123555 no se encuentra registrado.")

# d)
socio = {}
socio["dni"] = 40151724
socio["nombre"] = 'Esteban'
socio["apellido"] = 'Quito'
socio["edad"] = 17
socio["cuota"] = True
socios.append(socio)

# e)
mayor_edad = { "edad": -1 }
for s in socios:
    if s["edad"] > mayor_edad["edad"]:
        mayor_edad = s

print(f"e) DNI del socio de mayor edad: {mayor_edad['dni']}")

# f)
print("f)")
existe = False
socio_ind = 0
cuota = False
for i, s in enumerate(socios):
    if s["dni"] == 15188125:
        existe = True
        socio_ind = i
        if s["cuota"]:
            cuota = True
            
if existe:
    if cuota:
        del socios[socio_ind]
    else:
        print("No se puede dar de baja. El socio no pago su cuota.")
else:
    print("El socio de DNI 15.188.125 no existe.")

# g)
for i, s in enumerate(socios):
    if s["dni"] == 28731431:
        socios[i]["cuota"] = True
        break
        
print(socios)