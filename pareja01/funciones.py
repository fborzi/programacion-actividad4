# Dada la lista b = [ 4, "palabra", [0, 1], 9.6, False ]:
# Utilizar una instrucción para determinar si los siguientes elementos pertenecen a la lista:
# 9.6 0 False [0, 1] 4.0 "p"
# Utilizar una instrucción para determinar en qué posición (índice) se encuentra el elemento [0, 1].
b = [ 4, "palabra", [0, 1], 9.6, False ]
def verificar_elementos_y_posicion(lista):
    elementos_a_verificar =  lista
    resultados_verificacion = {elemento: (elemento in lista) for elemento in elementos_a_verificar}
    indice_elemento = lista.index([0, 1]) if [0, 1] in lista else -1
    return resultados_verificacion, indice_elemento

resultados, indice = verificar_elementos_y_posicion(b)
print("Resultados de verificación:", resultados)