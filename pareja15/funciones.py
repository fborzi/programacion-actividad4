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