def tiene_digitos_repetidos(numero):
    """Verifica si un número tiene dígitos repetidos"""
    digitos = str(numero)
    return len(digitos) != len(set(digitos))

def analizar_numeros():
    numeros_procesados = []
    continuar = True
    
    while continuar:
        try:
            num = int(input("Ingrese un número entero: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
        
        # verifica si el número tiene dígitos repetidos
        if not tiene_digitos_repetidos(num):
            print(f"¡Número {num} sin dígitos repetidos! Finalizando...")
            continuar = False
        else:
            numeros_procesados.append(num)
            
            # A. suma de dígitos que se repiten
            digitos = list(str(num))
            conteo = {}
            for digito in digitos:
                conteo[digito] = conteo.get(digito, 0) + 1
            
            digitos_repetidos = [int(d) for d, count in conteo.items() if count > 1]
            suma_repetidos = sum(digitos_repetidos)
            
            # B. cantidad de dígitos que se repiten
            cantidad_repetidos = len(digitos_repetidos)
            
            print(f"Número: {num}")
            print(f"A. Suma de dígitos repetidos: {suma_repetidos}")
            print(f"B. Cantidad de dígitos repetidos: {cantidad_repetidos}")
            print("-" * 40)
    
    # C. porcentaje de números mayores que 478
    if numeros_procesados:
        mayores_478 = [n for n in numeros_procesados if n > 478]
        porcentaje_mayores = (len(mayores_478) / len(numeros_procesados)) * 100
        
        # D. promedio de números procesados
        promedio = sum(numeros_procesados) / len(numeros_procesados)
        
        print("\n--- RESUMEN FINAL ---")
        print(f"C. Porcentaje de números > 478: {porcentaje_mayores:.2f}%")
        print(f"D. Promedio de números procesados: {promedio:.2f}")
        print(f"Total de números procesados: {len(numeros_procesados)}")
    else:
        print("No se procesaron números con dígitos repetidos.")

# ejecutar el programa
if __name__ == "__main__":
    analizar_numeros()