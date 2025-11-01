# 1️⃣ Crear el diccionario con los datos iniciales
habitantes = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

# 2️⃣ Informar la cantidad de habitantes de Pergamino
print("Habitantes de Pergamino:", habitantes["Pergamino"])

# 3️⃣ Agregar a Lincoln con 42.036 habitantes
habitantes["Lincoln"] = 42036

# 4️⃣ Eliminar a Junín
del habitantes["Junín"]

# 5️⃣ Incrementar los habitantes de Rojas en 1.000
habitantes["Rojas"] += 1000

# 6️⃣ Modificar la cantidad de habitantes de Pergamino por 91.399
habitantes["Pergamino"] = 91399

# 7️⃣ Mostrar el diccionario final
print("\nDatos actualizados:")
for ciudad, cantidad in habitantes.items():
    print(f"{ciudad}: {cantidad}")