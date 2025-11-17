# Almacenar el número de habitantes de cada ciudad en una estructura que te permita acceder directamente a dicho número sabiendo el nombre de la ciudad. Los datos son:

# Junín: 102.023, Rojas: 28.654, Pergamino: 80.569. Escribí instrucciones que permitan:
# Informar la cantidad de habitantes que tiene Pergamino.
# Agregar a Lincoln con 42.036 habitantes.
# Eliminar a Junín.
# Incrementar los habitantes de Rojas en 1.000.
# Modificar la cantidad de habitantes de Pergamino por 91.399.


import funciones

# Realizar las operaciones solicitadas
print(f"Habitantes de Pergamino: {funciones.informar_habitantes('Pergamino')}")
funciones.agregar_ciudad("Lincoln", 42036)
funciones.eliminar_ciudad("Junín")
funciones.incrementar_habitantes("Rojas", 1000)
funciones.modificar_habitantes("Pergamino", 91399)
