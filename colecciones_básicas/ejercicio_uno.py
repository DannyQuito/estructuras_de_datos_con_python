#Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.
# Pedimos la frase al usuario
frase = input("Ingresa una frase: ")

frase_minusc = frase.lower()

contador_vocales = 0
vocales = "aeiou"

for letra in frase_minusc:

    if letra in vocales:
        contador_vocales += 1  

print(f"La frase tiene {contador_vocales} vocales.")
