a = [False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True]

primero = a[0]

ultimo = a[-1]

print("Primero:", primero)

print("Último:", ultimo)

del a[0]

del a[-3:]

a.insert(0, 9)

indice_ix = a.index('ix')

a[indice_ix] = 4

a.append(5)

primeros_3 = a[:3]

print("Primeros 3 elementos:", primeros_3)

a.extend([a[:]])  # Usamos a[:] para copiar la lista original y evitar una referencia circular

print("'dos' está en la lista?", 'dos' in a)

print("3.0 está en la lista?", 3.0 in a)

print("'dos' está en la lista?", 'dos' in a)

print("3.0 está en la lista?", 3.0 in a)

print("Veces que aparece 1:", a.count(1))

print("Veces que aparece 4:", a.count(4))

for elem in a:
    print(elem)

for elem in reversed(a):
    print(elem)


