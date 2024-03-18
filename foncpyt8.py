def factorielle_naive(n):
    
    if n == 0:
        return 1
    else:
        F = 1
        for k in range(2, n + 1):
            F *= k
        return F

nombre = -5
resultat = factorielle_naive(nombre)
print(f"La factorielle de {nombre} est égale à {resultat}.")
