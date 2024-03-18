def est_premier(n):
    """
    Vérifie si un nombre est premier.

    Args:
        n (int): L'entier à vérifier.

    Returns:
        bool: True si le nombre est premier, False sinon.
    """
    if n < 2:
        return False  # Les nombres inférieurs à 2 ne sont pas premiers

    # Parcourir les nombres de 2 à la racine carrée de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Si n est divisible par i, il n'est pas premier

    return True  # Si aucun diviseur n'est trouvé, n est premier

# Exemple d'utilisation
nombre = 17
if est_premier(nombre):
    print(f"{nombre} est un nombre premier.")
else:
    print(f"{nombre} n'est pas un nombre premier.")
