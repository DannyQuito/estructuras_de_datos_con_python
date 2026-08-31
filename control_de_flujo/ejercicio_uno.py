#Leer un número N y mostrar los números del 1 al N.
# n = int(input("N: "))

# for i in range(1, n + 1):      # ¡ojo con el n+1!
#     print(i)

#Cámbialo para que muestre del N al 1 (hacia atrás). Pista: range(n, 0, -1).
n = int(input("N: "))

print(f"\nContando desde {n} hasta 1:")
# range(inicio, fin, paso)
for i in range(n, 0, -1):
    print(i)
