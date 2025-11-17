L = [5, 6, [9, 5], 2, 5]

def contar_5(lista):
    total = 0
    for elem in lista:
        if type(elem) == list:
            total += contar_5(elem)
        elif elem == 5:
            total += 1
    return total

print(f"La lista tiene {contar_5(L)} cincos")