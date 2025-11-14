# Convertir nombres a mayúsculas

# Lista del ejercicio anterior (use una ficticia)
a = [9, 1, 'dos', 4, 5, [9, 1, 'dos', 4, 5]]

print(f"\nLista original: {a}")

# Crear nueva lista con los strings convertidos a mayúsculas
nombres_mayusculas = [elemento.upper() if isinstance(elemento, str) else elemento for elemento in a]

print(f"\nLista con nombres en mayúsculas: {nombres_mayusculas}")