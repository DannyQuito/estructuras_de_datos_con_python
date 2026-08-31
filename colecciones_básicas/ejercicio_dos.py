#Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5], 
#calcula el promedio, la nota máxima y la mínima. 
#Imprime los tres valores con 2 decimales.

notas = [7, 8.5, 6, 9, 10, 5.5]
promedio = sum(notas) / len(notas)
maxima = max(notas)
minima = min(notas)
#ESULTADOS
print(f"Promedio: {promedio:.2f}")
print(f"Máxima:   {maxima:.2f}")
print(f"Mínima:   {minima:.2f}")


