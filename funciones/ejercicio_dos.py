# #Escribir una función que reciba un número y retorne True si es primo, False si no.
# def es_primo(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False           # sale inmediatamente
#     return True                    # llegó al final sin encontrar divisor

# # --- Uso 1: verificar uno ---
# num = int(input("Número: "))
# if es_primo(num):
#     print(f"{num} es primo")
# else:
#     print(f"{num} NO es primo")

# # --- Uso 2: listar primos entre 2 y 30 ---
# print("Primos entre 2 y 30:")
# for k in range(2, 31):
#     if es_primo(k):
#         print(k, end=" ")

#Escribe una función contar_primos(a, b) que cuente cuántos primos hay entre a y b.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False           
    return True                    

def contar_primos(a, b):
    contador = 0

    for k in range(a, b + 1):
        if es_primo(k): 
            contador += 1
    return contador

inicio = int(input("Ingrese el límite inicial (A): "))
fin = int(input("Ingrese el límite final (B): "))
total_primos = contar_primos(inicio, fin)
print(f"\nEntre {inicio} y {fin} hay exactamente {total_primos} números primos.")

