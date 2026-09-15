#Muestra los primeros N números de Fibonacci. 
# La serie: 0, 1, 1, 2, 3, 5, 8, 13, 21... 
# Cada número es la suma de los dos anteriores.
n = int(input("¿Cuántos? "))
a, b = 0, 1                         # asignación múltiple

for _ in range(n):                  # _ porque no usamos el índice
    print(a, end=" ")
    a, b = b, a + b                 # avanzamos la serie

print()                             # salto de línea final