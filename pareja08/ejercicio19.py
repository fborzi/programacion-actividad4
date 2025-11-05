'''19. Escribí un programa que solicite el ingreso de números enteros hasta leer uno que no tenga dígitos repetidos. Se pide informar:
a. Para cada número, la suma de los dígitos que se repiten en ese número.
b. Para cada número, la cantidad de dígitos que se repiten en ese número.
c. Al finalizar, el porcentaje de números procesados mayores que 478.
d. Al finalizar, el promedio de los números procesados.'''

from funciones import tiene_digitos_repetidos, suma_digitos_repetidos, cantidad_digitos_repetidos

numeros = []
mayores_478 = 0

while True:
    entrada = input("Ingresá un número entero: ")
    if not entrada.isdigit():
        print("Entrada inválida. Solo se aceptan números enteros positivos.")
        continue

    numero = int(entrada)
    numeros.append(numero)

    if not tiene_digitos_repetidos(numero):
        print("Este número no tiene dígitos repetidos. Fin del ingreso.")
        break

    suma = suma_digitos_repetidos(numero)
    cantidad = cantidad_digitos_repetidos(numero)

    print(f"Suma de dígitos repetidos: {suma}")
    print(f"Cantidad de dígitos repetidos: {cantidad}")

    if numero > 478:
        mayores_478 += 1

total = len(numeros)
porcentaje_mayores = (mayores_478 / total) * 100 if total > 0 else 0
promedio = sum(numeros) / total if total > 0 else 0

print("\n Estadísticas finales:")
print(f"Porcentaje de números mayores que 478: {porcentaje_mayores:.2f}%")
print(f"Promedio de los números ingresados: {promedio:.2f}")