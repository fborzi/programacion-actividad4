#EJER23

# Crear diccionario con datos iniciales
poblacion = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

print("Diccionario inicial de población:")
for ciudad, habitantes in poblacion.items():
    print(f"  {ciudad}: {habitantes:,} habitantes")

print("\n" + "="*60)

# a) Informar habitantes de Pergamino
print("\na) Habitantes de Pergamino:")
print(f"   {poblacion['Pergamino']:,} habitantes")

# b) Agregar Lincoln
print("\nb) Agregar Lincoln con 42.036 habitantes:")
poblacion["Lincoln"] = 42036
print(f"   Lincoln agregado: {poblacion['Lincoln']:,} habitantes")

# c) Eliminar Junín
print("\nc) Eliminar Junín:")
del poblacion["Junín"]
print("   Junín eliminado del diccionario")

# d) Incrementar habitantes de Rojas en 1.000
print("\nd) Incrementar habitantes de Rojas en 1.000:")
print(f"   Antes: {poblacion['Rojas']:,}")
poblacion["Rojas"] += 1000
print(f"   Después: {poblacion['Rojas']:,}")

# e) Modificar habitantes de Pergamino
print("\ne) Modificar habitantes de Pergamino a 91.399:")
print(f"   Antes: {poblacion['Pergamino']:,}")
poblacion["Pergamino"] = 91399
print(f"   Después: {poblacion['Pergamino']:,}")

# Mostrar diccionario final
print("\n" + "="*60)
print("Diccionario final de población:")
for ciudad, habitantes in poblacion.items():
    print(f"  {ciudad}: {habitantes:,} habitantes")
