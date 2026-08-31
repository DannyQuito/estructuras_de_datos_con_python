#Dado un texto, retorna un diccionario con la frecuencia de cada palabra
#(ignora mayúsculas). Al final, imprime la palabra que más se repite.

texto = "Python es un lenguaje de programacion y Python es muy facil de aprender"
conteo = {}
for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)
# Encontramos la palabra récord usando método key=conteo.get
mas = max(conteo, key=conteo.get)
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")
