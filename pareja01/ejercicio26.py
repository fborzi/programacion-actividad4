# Solicitá al usuario que ingrese nombres de ciudades y el país al que pertenecen (cortar cuando se ingresa la ciudad “zz”). Luego informá: cuántas ciudades ingresó en total y cuántas ciudades por cada país (para esto último, utilizá un diccionario). Hacé dos versiones diferentes del programa:
# En una de ellas las ciudades no se almacenarán a medida que se las ingresa.
# En la otra se almacenará cada ciudad con su país en una lista (cada elemento será una lista con 2 strings).

# Ejemplo: [ [“Colonia”, “Uruguay”], [“Granada”, “España”], [“Inverness”, “Escocia”], [“Salto”, “Uruguay”], [“Piriápolis”, “Uruguay”], [“Aberdeen”, “Escocia”] ]. Luego de haber terminado la carga de datos en la lista, se procesará la misma para calcular la cantidad de ciudades por país.

import funciones
# Ejecutar ambas versiones
print("=== Versión sin almacenamiento ===")
total, por_pais = funciones.version_sin_almacenamiento()
funciones.mostrar_resultados(total, por_pais)

print("\n=== Versión con almacenamiento ===")
total, por_pais = funciones.version_con_almacenamiento()
funciones.mostrar_resultados(total, por_pais)