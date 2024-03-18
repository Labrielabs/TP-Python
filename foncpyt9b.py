def tri_croissant():
    liste_nombres = []
    while True:
        try:
            saisie = input("Entrez un nombre (ou 'q' pour quitter) : ")
            if saisie.lower() == 'q':
                break
            nombre = float(saisie)
            liste_nombres.append(nombre)
        except ValueError:
            print("Veuillez entrer un nombre valide ou 'q' pour quitter.")

    liste_nombres_triee = sorted(liste_nombres)
    return liste_nombres_triee

# Exemple d'utilisation
resultat = tri_croissant()
print("Liste triée :", resultat)
