def suma_digitos(n):
    return sum(int(d) for d in str(n))

def sumatoria_digitos(lista):
    return [suma_digitos(num) for num in lista]

print(sumatoria_digitos([154, 27890, 111, 43]))

