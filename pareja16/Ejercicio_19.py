
from funciones import digitos_repetidos

contador = 0
acumulador = 0
mayores_478 = 0

# primer número
n = int(input("Ingresar numero: "))
repetidos = digitos_repetidos(n)

# mientras el número tenga dígitos repetidos sigo pidiendo números
while len(repetidos) != 0:
    contador += 1
    acumulador += n
    if n > 478:
        mayores_478 += 1

    print("Suma dígitos repetidos:", sum(int(x) for x in repetidos))
    print("Cantidad dígitos repetidos:", len(repetidos))

    n = int(input("Ingresar numero: "))
    repetidos = digitos_repetidos(n)

# el que corta también se procesa (pero con 0 en repetidos)
contador += 1
acumulador += n
if n > 478:
    mayores_478 += 1

print("Suma dígitos repetidos:", 0)
print("Cantidad dígitos repetidos:", 0)

# informe final
print(" Informe Final ")
print("Porcentaje mayores a 478:", (mayores_478*100)/contador, "%")
print("Promedio:", acumulador/contador)

