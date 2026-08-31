#Leer tres notas de un estudiante y mostrar su promedio.
# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# n3 = float(input("Nota 3: "))

# promedio = (n1 + n2 + n3) / 3      # PROCESO en una línea

# print(f"Promedio: {promedio:.1f}")  # :.1f muestra un decimal

#Modifícalo para que muestre «Aprueba» si el promedio es ≥ 7 y «Reprueba» si no. (Necesitas el if del módulo 3).
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

promedio = (n1 + n2 + n3) / 3      # PROCESO en una línea
if (promedio >= 7):
    print(f"El estudiantes si aprueba. Nota Promedio= {promedio:.1f}")
else:
    print(f"El estudiantes NO aprueba. Nota Promedio= {promedio:.1f} ")
