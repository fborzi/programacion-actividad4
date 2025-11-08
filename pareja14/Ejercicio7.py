def dos_minimos(lista):

	# Caso vacío
	if not lista:
		return (None, None)

	min1 = None
	min2 = None

	for x in lista:
		# Si aún no hay min1, o encontramos un valor menor, lo movemos a min1 y desplazamos el anterior a min2
		if min1 is None or x < min1:
			min2 = min1
			min1 = x
		# Si x no es menor que min1 pero es menor que min2 (o min2 no existe), actualizamos min2
		elif min2 is None or x < min2:
			min2 = x

	return (min1, min2)


if __name__ == "__main__":
	# Demostración
	ejemplos = [
		[23, 456, 12, 16, -4, 56],
		[4],
		[]
	]

	for e in ejemplos:
		print(f"dos_minimos({e}) -> {dos_minimos(e)}")
