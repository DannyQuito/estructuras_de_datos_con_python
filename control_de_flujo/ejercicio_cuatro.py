#Leer las notas de N estudiantes (una por una) y contar cuántos aprobaron (nota ≥ 70).
# n = int(input("¿Cuántos estudiantes? "))
# aprobados = 0                       # contador arranca en 0

# for i in range(n):
#     nota = float(input(f"Nota {i+1}: "))
#     if nota >= 7:                   # el 7 es el umbral (o 70 si es sobre 100)
#         aprobados += 1              # aumenta solo si aprobó

# print(f"Aprobados: {aprobados} de {n}")

#Añade un contador para reprobados y muestra el porcentaje de aprobación.
n = int(input("¿Cuántos estudiantes? "))
aprobados = 0                       
reprobados = 0 

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 70:                   
        aprobados += 1              
    else:
        reprobados += 1

porcentaje_aprobacion = (aprobados / n) * 100

# --- MOSTRAR RESULTADOS ---
print(f"\nAprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Porcentaje de aprobación: {porcentaje_aprobacion:.2f}%")

