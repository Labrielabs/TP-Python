import math

def produit(a, b):
    """
    Calcule le produit de deux nombres.
    
    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.
    
    Returns:
        float: Produit des deux nombres.
    """
    return math.prod([a, b])

# Exemple d'utilisation
nombre1 = 5
nombre2 = 3
resultat = produit(nombre1, nombre2)
print(f"Le produit de {nombre1} et {nombre2} est égal à {resultat}.")
