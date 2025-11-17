def ocurrencias(lista):
    
    #si la lista esta vacia, retorna una lista vacia
    if not lista:
        return[]
    
    #lista final que se devuelve
    resultado = []
    #primer elemento de la lista
    elemento_actual = lista[0]
    #contador de repeticiones
    contador = 1

    #recorre desde el segundo elemento
    for i in range(1, len(lista)):
        if lista[i] == elemento_actual:
            contador +=1 #suma el elemento que se repite
        
        else:
            #agregar el elemento con su cantidad al resultado
            resultado.append([elemento_actual,contador])
            #nuevo elemento
            elemento_actual = lista[i]
            #se reinicia el contador
            contado = 1

            #se agrega el ultimo grupo pendiente
            resultado.append([elemento_actual,contador])
            
            #retorna al resulado
            return resultado
        
#Ejemplo
print(ocurrencias(['z', 7, True, True, 34, 'z', 'z', 'z', 3.14]))
        