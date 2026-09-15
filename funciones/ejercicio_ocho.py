#Función factorial(n) y luego combinatoria(n, k) = n! / (k! · (n-k)!).
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def combinatoria(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Uso
print(factorial(5))            # 120
print(combinatoria(5, 2))      # 10 = 5!/(2!·3!) = 120/12