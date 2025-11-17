from Funciones import verificar_pertenencia, obtener_indice

# Lista dada
b = [4, "palabra", [0, 1], 9.6, False]

# Elementos a verificar
elementos_a_buscar = [9.6, 0, False, [0, 1], 4.0, "p"]

# Verificar si pertenecen
verificar_pertenencia(b, elementos_a_buscar)

# Determinar el índice del elemento [0, 1]
obtener_indice(b, False)




