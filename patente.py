def saisir_liste():
    """
    Saisit une liste d'entiers à partir de l'entrée utilisateur.
    L'utilisateur doit d'abord donner la taille de la liste.
    """
    try:
        taille = int(input("Entrez la taille de la liste : "))
        ma_liste = []  # Crée une liste vide

        for i in range(taille):
            element = int(input(f"Entrez l'élément {i + 1} : "))
            ma_liste.append(element)  # Ajoute l'élément à la liste

        return ma_liste
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

# Exemple d'utilisation :
if __name__ == "__main__":
    liste_utilisateur = saisir_liste()
    print("La liste saisie est :", liste_utilisateur)
