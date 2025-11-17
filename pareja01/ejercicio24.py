# Se ingresan todos los datos de los socios del club 'CAVUL'. Para cada socio se solicita: Nombre, apellido, DNI, edad y si tiene o no su cuota al día. La lectura de los datos finaliza cuando se ingresa el DNI '0'. Almacenar la información de los socios en una estructura adecuada para realizar búsquedas por DNI. Se pide:
# Informar la cantidad de socios del club.
# Informar la cantidad de socios morosos.
# Informar el nombre y apellido del socio cuyo DNI es 25.123.555. En caso que no exista un socio con dicho documento, se deberá informar la situación.
# Dar de alta a un nuevo socio cuyos datos son: DNI: 40.151.724, apellido: 'Quito', nombre: 'Esteban' y edad: 17. Dicho socio acaba de pagar su cuota inicial.
# Informar el número de documento del socio de mayor edad.
# Dar de baja al socio con el DNI 15.188.125, asegurándose primero que esa persona efectivamente sea socio del club. No deberá aceptarse la baja del socio si éste no tiene su cuota al día.
# Registrar que el socio cuyo DNI es 28.731.431 acaba de pagar la cuota de este mes.

import funciones 

socios = funciones.ingresar_socios()

print(f"\nCantidad de socios: {funciones.cantidad_socios(socios)}")
print(f"Cantidad de morosos: {funciones.cantidad_morosos(socios)}")
print(f"\nBuscando socio 25123555: {funciones.buscar_socio(socios, '25123555')}")

funciones.agregar_socio(socios, '40151724', 'Esteban', 'Quito', 17, True)

print(f"\nDNI del socio de mayor edad: {funciones.socio_mayor_edad(socios)}")

print(f"\nIntentando dar de baja al socio 15188125:")
print(funciones.dar_baja_socio(socios, '15188125'))


print(f"\nRegistrando pago de cuota del socio 28731431:")
print(funciones.pagar_cuota(socios, '28731431'))