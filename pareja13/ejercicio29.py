def sucesion_mira_y_deci(n):
    """
    Genera los primeros n números de la sucesión 'Mirá y Decí' (Look-and-Say).
    
    Parámetros:
        n (int): cantidad de términos a generar.
        
    Retorna:
        lista de strings con los primeros n términos de la sucesión.
    """
    if n <= 0:
        return []

    resultado = ["1"]  # primer número de la sucesión

    while len(resultado) < n:
        anterior = resultado[-1]
        siguiente = ""
        i = 0
        while i < len(anterior):
            conteo = 1
            # contar repeticiones consecutivas del mismo dígito
            while i + 1 < len(anterior) and anterior[i] == anterior[i + 1]:
                conteo += 1
                i += 1
            siguiente += str(conteo) + anterior[i]
            i += 1
        resultado.append(siguiente)

    # convertir los números a int si se desea (en este ejemplo, se usan strings para preservar dígitos grandes)
    return resultado

# Ejemplo de uso:
print(sucesion_mira_y_deci(9))
