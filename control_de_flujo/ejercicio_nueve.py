#Lee N números y muestra la suma de los pares y la suma de los impares por separado.
n = int(input("¿Cuántos números? "))
suma_pares = 0
suma_impares = 0

for i in range(n):
    x = int(input(f"Número {i+1}: "))
    if x % 2 == 0:
        suma_pares += x
    else:
        suma_impares += x

print(f"Suma pares: {suma_pares}")
print(f"Suma impares: {suma_impares}")