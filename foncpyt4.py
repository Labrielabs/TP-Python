def pgcd(a, b):
    """
    Calcule le PGCD de deux entiers en utilisant l'algorithme d'Euclide.
    
    Args:
        a (int): Premier entier.
        b (int): Deuxième entier.
    
    Returns:
        int: PGCD des deux entiers.
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Exemple d'utilisation
nombre1 = 24
nombre2 = 36
resultat = pgcd(nombre1, nombre2)
print(f"Le PGCD de {nombre1} et {nombre2} est égal à {resultat}.")
