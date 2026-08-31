#Leer un número y determinar si es primo (solo divisible entre 1 y él mismo).
# n = int(input("Número: "))
# es_primo = True                     # BANDERA: asumimos que sí

# if n < 2:
#     es_primo = False                # 0 y 1 no son primos
# else:
#     # Probar divisores del 2 hasta √n
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:              # si i divide exacto a n...
#             es_primo = False        # ...no es primo
#             break                   # optimización: no seguir probando

# if es_primo:
#     print(f"{n} es primo")
# else:
#     print(f"{n} NO es primo")

#Genera una lista de todos los primos entre 2 y 100.

# Creamos una lista vacía para almacenar los números primos que encontremos
primos_2_al_100 = []

for n in range(2, 101):
    es_primo = True  
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break  # Si encuentra un divisor
            
    if es_primo:
        primos_2_al_100.append(n)


print("Lista de números primos entre 2 y 100:")
print(primos_2_al_100)
