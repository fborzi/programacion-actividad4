#Ejercicio22
#  Crear el diccionario con las ciudades y sus habitantes
habitantes = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

# a) Informar la cantidad de habitantes que tiene Pergamino
print("La cantidad de habitantes de Pergamino es:", habitantes["Pergamino"])

# b) Agregar a Lincoln con 42.036 habitantes
habitantes["Lincoln"] = 42036

# c) Eliminar a Junín
del habitantes["Junín"]

# d) Incrementar los habitantes de Rojas en 1.000
habitantes["Rojas"] = habitantes["Rojas"] + 1000

# e) Modificar la cantidad de habitantes de Pergamino por 91.399
habitantes["Pergamino"] = 91399

print("Diccionario actualizado de habitantes:", habitantes)
