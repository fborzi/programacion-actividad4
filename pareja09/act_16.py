# 1 Creamos el conjunto numeros
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 2. agregamos el once y el doce
numeros.add(11)
numeros.add(12)

# 3. Actualizar la estructura incorporando los números del 30 al 35.
# La forma eficiente es usar .update() y un generador o una lista/rango.
numeros.update(range(30, 36)) # range(30, 36) incluye 30, 31, 32, 33, 34, 35

# 4. Agregar los números 232 y -264.
numeros.add(232)
numeros.add(-264)

print(f"Conjunto final: {numeros}")