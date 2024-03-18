def calculer_moyenne_liste():
    """
    Saisit une liste d'entiers à partir de l'entrée utilisateur et calcule la moyenne.
    """
    try:
        taille = int(input("Entrez la taille de la liste : "))
        # Crée une liste vide

        ma_liste = []  
        for i in range(taille):
            element = int(input(f"Entrez l'élément {i + 1} : "))
            ma_liste.append(element)  # Ajoute l'élément à la liste

        # Calcul de la moyenne
        somme = sum(ma_liste)
        moyenne = somme / len(ma_liste)

        return moyenne
    except ValueError:
        print("Veuillez entrer des nombres entiers valides.")

# Exemple d'utilisation :
if __name__ == "__main__":
    moyenne_resultat = calculer_moyenne_liste()
    print(f"La moyenne des éléments de la liste est : {moyenne_resultat:.2f}")
