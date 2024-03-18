def est_pair(nombre):
    """
    Vérifie si un nombre est pair.
    
    Args:
        nombre (int): L'entier à vérifier.
    
    Returns:
        bool: True si le nombre est pair, False sinon.
    """
    try:
        nombre = int(nombre)  # Convertir l'entrée en entier
        if nombre % 2 == 0:
            return True
        else:
            return False
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
        return False

# Exemple d'utilisation
entree_utilisateur = input("Entrez un nombre entier : ")
if est_pair(entree_utilisateur):
    print(f"{entree_utilisateur} est pair.")
else:
    print(f"{entree_utilisateur} est impair.")

