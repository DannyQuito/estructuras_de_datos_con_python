#Escribir una función suma_digitos(n) que retorne la suma de los dígitos de un número.
# def suma_digitos(n):
#     n = abs(n)                     # por si es negativo
#     suma = 0
#     while n > 0:
#         suma += n % 10             # último dígito
#         n = n // 10                # quita el último dígito
#     return suma

# # Uso
# num = int(input("Número: "))
# print(f"Suma: {suma_digitos(num)}")

# # También sirve para varios
# for x in [123, 4783, 999]:
#     print(f"{x} → {suma_digitos(x)}")

#Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus dígitos
# elevados al número de dígitos. Ej.: 153 = 1³+5³+3³.

def suma_digitos(n):
    n = abs(n)
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma

def es_narcisista(n):
    texto = str(n)               
    num_digitos = len(texto)     
    suma_potencias = 0
    
    # Recorremos cada dígito de la cadena de texto
    for digito_texto in texto:
        digito_entero = int(digito_texto)     
        suma_potencias += digito_entero ** num_digitos  
        
    return suma_potencias == n


numero_prueba = int(input("Ingresa un número para verificar si es narcisista: "))

if es_narcisista(numero_prueba):
    print(f"¡Sí! {numero_prueba} es un número narcisista.")
else:
    print(f"No, {numero_prueba} no es narcisista.")

print("\nVerificando una lista de números:")
for x in [153, 370, 125, 407, 9]:
    print(f"¿Es {x} narcisista? → {es_narcisista(x)}")




