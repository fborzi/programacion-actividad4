from collections import Counter

total_numeros = 0
mayores_478 = 0
suma_total = 0

while True:
    n = int(input("Ingresá un número entero: "))
    total_numeros += 1
    suma_total += n

    # Convertimos a string para analizar dígitos
    digitos = [int(d) for d in str(abs(n))]  # abs por si hay negativos
    contador = Counter(digitos)

    # Filtramos los dígitos que se repiten
    repetidos = [d for d, c in contador.items() if c > 1]

    if n > 478:
        mayores_478 += 1

    if repetidos:
        suma_repetidos = sum(repetidos)
        cantidad_repetidos = len(repetidos)
        print(f"Suma de dígitos repetidos: {suma_repetidos}")
        print(f"Cantidad de dígitos repetidos: {cantidad_repetidos}")
    else:
        print("No hay dígitos repetidos. Fin del programa.")
        break

# Cálculos finales
porcentaje_mayores = (mayores_478 / total_numeros) * 100
promedio = suma_total / total_numeros

print("\n--- Resultados finales ---")
print(f"Porcentaje de números > 478: {porcentaje_mayores:.2f}%")
print(f"Promedio de los números procesados: {promedio:.2f}")
