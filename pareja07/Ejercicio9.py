def digitos(numero):
    return [int(d) for d in str(abs(numero))]

print(digitos(12345))   
print(digitos(-987))    
