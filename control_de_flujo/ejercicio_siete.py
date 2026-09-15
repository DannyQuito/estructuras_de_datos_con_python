#Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
n = int(input("Tabla de: "))

for i in range(1, 13):
    print(f"{n} × {i} = {n * i}")