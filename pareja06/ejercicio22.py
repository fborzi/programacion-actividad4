"""
 Ejercicio 22:
 Diccionario de habitantes por ciudad
"""

print("=== HABITANTES POR CIUDAD ===")
print()

# Creamos el diccionario con los datos iniciales
# Clave: nombre de ciudad, Valor: número de habitantes
habitantes = {
    "Junín": 102023,
    "Rojas": 28654,
    "Pergamino": 80569
}

print("Diccionario inicial:")
print(habitantes)
print()

# a) Informar la cantidad de habitantes que tiene Pergamino
print("a) Cantidad de habitantes de Pergamino:")
print(f"   Pergamino tiene {habitantes['Pergamino']} habitantes")
print()

# b) Agregar a Lincoln con 42.036 habitantes
print("b) Agregar Lincoln:")
habitantes["Lincoln"] = 42036
print(f"   Lincoln agregada con {habitantes['Lincoln']} habitantes")
print(f"   Diccionario: {habitantes}")
print()

# c) Eliminar a Junín
print("c) Eliminar Junín:")
del habitantes["Junín"]  # También se puede usar: habitantes.pop("Junín")
print(f"   Junín eliminada del diccionario")
print(f"   Diccionario: {habitantes}")
print()

# d) Incrementar los habitantes de Rojas en 1.000
print("d) Incrementar habitantes de Rojas en 1.000:")
print(f"   Rojas antes: {habitantes['Rojas']} habitantes")
habitantes["Rojas"] += 1000
print(f"   Rojas después: {habitantes['Rojas']} habitantes")
print(f"   Diccionario: {habitantes}")
print()

# e) Modificar la cantidad de habitantes de Pergamino por 91.399
print("e) Modificar habitantes de Pergamino:")
print(f"   Pergamino antes: {habitantes['Pergamino']} habitantes")
habitantes["Pergamino"] = 91399
print(f"   Pergamino después: {habitantes['Pergamino']} habitantes")
print(f"   Diccionario: {habitantes}")
print()

# === RESUMEN FINAL ===
print("=" * 50)
print("DICCIONARIO FINAL:")
print()
for ciudad, poblacion in habitantes.items():
    print(f"   {ciudad}: {poblacion:,} habitantes".replace(",", "."))

print()
print(f"Total de ciudades en el diccionario: {len(habitantes)}")
print()

# === INFORMACIÓN ADICIONAL ===
print("=" * 50)
print("OPERACIONES CON DICCIONARIOS:")
print()
print("• Acceder a un valor: diccionario['clave']")
print("• Agregar/Modificar: diccionario['clave'] = valor")
print("• Eliminar: del diccionario['clave'] o diccionario.pop('clave')")
print("• Verificar existencia: 'clave' in diccionario")
print("• Obtener todas las claves: diccionario.keys()")
print("• Obtener todos los valores: diccionario.values()")
print("• Obtener pares clave-valor: diccionario.items()")