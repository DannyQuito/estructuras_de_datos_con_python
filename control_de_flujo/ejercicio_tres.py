#Leer N y calcular el factorial (N! = 1 × 2 × 3 × ... × N). Ejemplo: 5! = 120.
n = int(input("N: "))
fact = 1                    # INICIALIZACIÓN: 1 porque vamos a multiplicar

for i in range(1, n + 1):
    fact = fact * i         # o: fact *= i

print(f"{n}! = {fact}")

#¿Qué pasa con N muy grande (100!)? Python maneja enteros infinitos, pruébalo. En JS con enteros normales explotaría.
