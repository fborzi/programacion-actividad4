from funciones import digitos_repetidos

contador = 0
mayores_478 = 0
suma_total = 0

# Leer primer número
n = int(input("Ingresá un número entero: "))
repetidos = digitos_repetidos(n)

# El bucle continúa mientras haya dígitos repetidos
while len(repetidos) > 0:
    contador += 1
    suma_total += n

    print(f"Suma de los dígitos repetidos: {sum(repetidos)}")
    print(f"Cantidad de dígitos repetidos: {len(repetidos)}")

    if n > 478:
        mayores_478 += 1

    n = int(input("Ingresá un número entero: "))
    repetidos = digitos_repetidos(n)

# Si salimos del bucle, el último número no tiene dígitos repetidos
contador += 1
suma_total += n
if n > 478:
    mayores_478 += 1
print("Este número no tiene dígitos repetidos. Fin del programa.")

# Cálculos finales
porcentaje_mayores = (mayores_478 / contador) * 100
promedio = suma_total / contador

print("\n--- Resultados finales ---")
print(f"Porcentaje de números mayores que 478: {porcentaje_mayores:.2f}%")
print(f"Promedio de los números ingresados: {promedio:.2f}")
