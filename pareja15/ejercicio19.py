# Números con dígitos repetidos

print("\nIngrese números enteros.")
print("El programa finalizará cuando ingrese un número sin dígitos repetidos.\n")

numeros_procesados = []
mayores_que_478 = 0

def tiene_digitos_repetidos(numero):
    """Verifica si un número tiene dígitos repetidos"""
    digitos_str = str(abs(numero))
    return len(digitos_str) != len(set(digitos_str))

def analizar_numero(numero):
    """Analiza un número y retorna información sobre sus dígitos repetidos"""
    digitos_str = str(abs(numero))
    conteo_digitos = {}
    
    for digito in digitos_str:
        conteo_digitos[digito] = conteo_digitos.get(digito, 0) + 1
    
    digitos_repetidos = {d: c for d, c in conteo_digitos.items() if c > 1}
    
    suma_repetidos = sum(int(d) * c for d, c in digitos_repetidos.items())
    cantidad_repetidos = len(digitos_repetidos)
    
    return suma_repetidos, cantidad_repetidos

# Leer números hasta encontrar uno sin dígitos repetidos
continuar = True
while continuar:
    try:
        numero = int(input("Ingrese un número entero: "))
        
        if tiene_digitos_repetidos(numero):
            numeros_procesados.append(numero)
            
            #  Analizar dígitos repetidos
            suma_repetidos, cantidad_repetidos = analizar_numero(numero)
            print(f"  Suma de dígitos repetidos: {suma_repetidos}")
            print(f"  Cantidad de dígitos que se repiten: {cantidad_repetidos}")
            
            # Contar si es mayor que 478
            if numero > 478:
                mayores_que_478 += 1
        else:
            print(f"\nEl número {numero} no tiene dígitos repetidos. Finalizando...\n")
            continuar = False
            
    except ValueError:
        print("Error: Ingrese un número entero válido")

# Porcentaje de números mayores que 478
if numeros_procesados:
    porcentaje = (mayores_que_478 / len(numeros_procesados)) * 100
    print(f"c) Porcentaje de números mayores que 478: {porcentaje:.2f}%")
    
    # Promedio de los números procesados
    promedio = sum(numeros_procesados) / len(numeros_procesados)
    print(f"d) Promedio de los números procesados: {promedio:.2f}")
else:
    print("No se procesaron números con dígitos repetidos.")