def calculer_moyenne_des_eleves(liste):

    if len(liste) == 0:
        return 0       #Pour ne pas diviser par 0 et avoir une erreur
    total = sum(liste)
    moyenne = total / len(liste)
    return moyenne

ma_liste = [44, 89, 65, 99, 22]
resultat = calculer_moyenne_des_eleves(ma_liste)
print(f"La moyenne de la liste est : {resultat:.2f}")
