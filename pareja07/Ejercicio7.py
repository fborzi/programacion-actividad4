def dos_minimos(lista):
    if not lista:
        return (None, None)
    if len(lista) == 1:
        return (lista[0], None)
    
    min1, min2 = sorted(lista[:2])
    
    for elem in lista[2:]:
        if elem < min1:
            min2 = min1
            min1 = elem
        elif elem < min2:
            min2 = elem
            
    return (min1, min2)


print(dos_minimos([23, 456, 12, 16, -4, 56]))  
print(dos_minimos([4]))                        
print(dos_minimos([]))                         
