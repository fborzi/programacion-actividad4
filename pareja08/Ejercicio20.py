cadena = input("Ingrese un texto: ")

palabras = cadena.lower().split(" ")
palabras_res = []
for p in palabras:
    if p != "":
        palabras_res.append(p)

print(f"El texto ingresado contiene {len(palabras_res)} palabras.")

abecedario = "qwertyuiopasdfghjklñzxcvbnm"
for p in palabras_res:
    letras = {}
    for l in p:
        if l in abecedario:
            if not l in letras:
                letras[l] = 1
            else:
                letras[l] += 1
            
    print(f"Letras repetidas en {p}:")
    switch = False
    for i in letras:
        if letras[i] > 1:
            print(f"● {i}")
            switch = True
    if not switch:
        print("La palabra no tiene letras repetidas.")