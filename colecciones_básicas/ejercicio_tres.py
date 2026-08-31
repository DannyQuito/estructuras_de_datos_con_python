#Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados 
#respetando el orden de la primera aparición. 

lista_original = ["a", "b", "a", "c", "b", "d"]
lista_sin_duplicados = []

vistos = set()

for elemento in lista_original:
    # Si el elemento NO ha sido visto antes...
    if elemento not in vistos:
        lista_sin_duplicados.append(elemento)
        vistos.add(elemento)                    

print(f"Original:       {lista_original}")
print(f"Sin duplicados: {lista_sin_duplicados}")





