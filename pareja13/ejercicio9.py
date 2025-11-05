def digitos(numero):

    numero = str(numero)
    lista_digitos = [int(d) for d in numero]
    return lista_digitos

print (digitos(3564))