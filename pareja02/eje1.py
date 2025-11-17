#EJE1

# Lista dada
b = [4, "palabra", [0, 1], 9.6, False]

# Elementos a verificar
elementos_a_verificar = [9.6, 0, False, [0, 1], 4.0, "p"]

print("Lista b:", b)
print("\nVerificando pertenencia de elementos:\n")

for elemento in elementos_a_verificar:
    if elemento in b:
        print(f"✓ {repr(elemento)} SÍ pertenece a la lista")
    else:
        print(f"✗ {repr(elemento)} NO pertenece a la lista")

print("\n" + "="*60)
print("Explicación:")
print("- 9.6 está en la lista")
print("- 0 NO está en la lista (solo está dentro de [0, 1])")
print("- False está en la lista")
print("- [0, 1] está en la lista como un elemento completo")
print("- 4.0 NO está en la lista (4 es int, no float)")
print("- 'p' NO está en la lista (solo está dentro de 'palabra')")
