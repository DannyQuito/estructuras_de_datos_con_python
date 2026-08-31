#Leer las notas de N estudiantes y mostrar la nota más alta.
# n = int(input("¿Cuántas notas? "))
# maxima = float("-inf")              # valor imposible: nada será menor

# for i in range(n):
#     nota = float(input(f"Nota {i+1}: "))
#     if nota > maxima:               # ¿es mayor que el récord?
#         maxima = nota               # sí → actualizamos

# print(f"Máxima: {maxima}")

#Adaptarlo para encontrar la menor nota. Cambio: float("inf") y if nota < minima:.
n = int(input("¿Cuántas notas? "))
minima = float("inf")  # Inicializamos en infinito positivo (nada será mayor que esto)

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota < minima:  # ¿Es menor que nuestro récord actual?
        minima = nota  # Sí -> actualizamos la nota menor

print(f"Mínima: {minima}")
