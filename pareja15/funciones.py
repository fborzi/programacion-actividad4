#Ejercicio 6 
"""Función que recibe una lista y devuelve el elemento mínimo de la lista. Si la lista está vacía, devuelve None.
 @param lista: Lista de elementos comparables.
 return: El elemento mínimo de la lista o None si la lista está vacía.
"""
def minimo_elemento(lista):
    if not lista:
        return None  # Manejar lista vacía
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo