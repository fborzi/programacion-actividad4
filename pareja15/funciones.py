#Ejercicio 6 
"""Función que recibe una lista y devuelve el elemento mínimo de la lista. Si la lista está vacía, devuelve None.
 @param lista: Lista de elementos comparables.
 return: El elemento mínimo de la lista o None si la lista está vacía.
"""
def minimo_elemento(lista):
    if not lista:
        return None   
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo

#Ejercicio8
"""Función que simula el juego de piedra, papel o tijera.
 @param uno: Elección del primer jugador ('piedra', 'papel' o 'tijera').
 @param dos: Elección del segundo jugador ('piedra', 'papel' o 'tijera').
 return: 1 si gana el primer jugador, 2 si gana el segundo jugador, 0 en caso de empate.
"""
def piedra_papel_tijera(uno, dos):
    uno = uno.lower()
    dos = dos.lower()
    
    if uno == dos:
        return 0
    
    if (uno == 'piedra' and dos == 'tijera') or \
       (uno == 'tijera' and dos == 'papel') or \
       (uno == 'papel' and dos == 'piedra'):
        return 1
    
    return 2

#Ejercicio10
"""Función que elimina los elementos adyacentes repetidos en una lista.
     @param lista: Lista de elementos.
     return: Nueva lista sin elementos adyacentes repetidos.
"""
def borrar_adyacentes(lista):
    if not lista:
        return []
    
    resultado = [lista[0]]
    
    for elemento in lista[1:]:
        if elemento != resultado[-1]:
            resultado.append(elemento)
    
    return resultado

#Ejercicio12
"""Función que retorna una lista con la suma de los dígitos de cada número en la lista dada.
     @param lista: Lista de números enteros.
     return: Nueva lista con la suma de los dígitos de cada número."""
# Función que suma los dígitos de un número
def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10   
        n //= 10          
    return suma

# Función que aplica la suma de dígitos a cada número de la lista
def sumatoria_digitos(lista):
    resultado = []
    for numero in lista:
        resultado.append(suma_digitos(numero))
    return resultado