# Función sucesion_mira_y_deci

from funciones import sucesion_mira_y_deci


# Pruebas de la función sucesion_mira_y_deci
print("\nPruebas de la función sucesion_mira_y_deci():")

n1 = 9
resultado1 = sucesion_mira_y_deci(n1)
print(f"\nsucesion_mira_y_deci({n1}):")
print(resultado1)

print("\nDesglose de la sucesión:")
for i, numero in enumerate(resultado1, 1):
    print(f"{i}. {numero}")

