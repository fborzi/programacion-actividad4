"""
EJERCICIO 6: Convertir nombres a mayúsculas
Producir una nueva lista con los nombres convertidos a mayúsculas
(usando la lista del ejercicio anterior)
"""

# Para este ejercicio, simularemos una lista de nombres
# En un caso real, se usaría la lista del ejercicio 5
nombres = ["Juan", "María", "Pedro", "Ana", "Carlos"]

print("Lista original de nombres:")
for nombre in nombres:
    print(f"  - {nombre}")

# Crear nueva lista con nombres en mayúsculas
nombres_mayusculas = [nombre.upper() for nombre in nombres]

print("\nLista de nombres en MAYÚSCULAS:")
for nombre in nombres_mayusculas:
    print(f"  - {nombre}")
