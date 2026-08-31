#Leer N y calcular la suma de 1 + 2 + 3 + ... + N.
# n = int(input("N: "))
# suma = 0                    # INICIALIZACIÓN del acumulador

# for i in range(1, n + 1):
#     suma = suma + i         # equivale a: suma += i

# print(f"Suma: {suma}")

#Adaptarlo para calcular la suma de los pares del 2 al 100. Pista: range(2, 101, 2).
# el ejercicio pide del 2 al 100 fijos.
suma_pares = 0 
for i in range(2, 101, 2):
    suma_pares += i  # Vamos sumando cada número par

print(f"La suma de los números pares del 2 al 100 es: {suma_pares}")
