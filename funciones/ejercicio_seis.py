#Función maximo(a, b, c) que retorne el mayor de tres números.
def maximo(a, b, c):
    return max(a, b, c)         # Python trae max()

# O manualmente:
def maximo_manual(a, b, c):
    mayor = a
    if b > mayor: mayor = b
    if c > mayor: mayor = c
    return mayor

print(maximo(5, 9, 3))          # 9
print(maximo_manual(5, 9, 3))   # 9