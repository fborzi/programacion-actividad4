# ===== main.py =====
from Funciones import cargar_ciudades_sin_lista

dic = {}
total = cargar_ciudades_sin_lista(dic)

print("Total de ciudades:", total)
print("Ciudades por país:", dic)
