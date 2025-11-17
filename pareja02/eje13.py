#EJE13

from Funcioness import suma_digitos, sumatoria_digitos

print("Pruebas de las funciones:\n")

# Prueba de suma_digitos
print("Función suma_digitos():")
numeros = [154, 27890, 111, 43]
for num in numeros:
    print(f"  suma_digitos({num}) = {suma_digitos(num)}")

print("\n" + "="*50)

# Prueba de sumatoria_digitos
print("\nFunción sumatoria_digitos():")
lista = [154, 27890, 111, 43]
resultado = sumatoria_digitos(lista)
print(f"Lista:     {lista}")
print(f"Resultado: {resultado}")

print("\nExplicación:")
print("  154 → 1+5+4 = 10")
print("  27890 → 2+7+8+9+0 = 26")
print("  111 → 1+1+1 = 3")
print("  43 → 4+3 = 7")
