def moyenne(liste_nombres):
    """
    Calcule la moyenne d'une liste de nombres.
    
    Args:
        liste_nombres (list): Liste de nombres.
    
    Returns:
        float: Moyenne des nombres dans la liste.
    """
    somme_nombres = sum(liste_nombres)
    nombre_elements = len(liste_nombres)
    moyenne = somme_nombres / nombre_elements
    return moyenne

# Exemple d'utilisation
mes_nombres = [10, 20, 30, 40, 50]
resultat_moyenne = moyenne(mes_nombres)
print(f"La moyenne des nombres {mes_nombres} est égale à {resultat_moyenne:.2f}.")
