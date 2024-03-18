# Créer une liste vide pour stocker les informations des étudiants
etudiants = []

# Demander à l'utilisateur combien d'étudiants il souhaite ajouter
nombre_etudiants = int(input("Combien d'étudiants souhaitez-vous ajouter ? "))

# Boucle pour saisir les informations de chaque étudiant
for i in range(nombre_etudiants):
    print(f"\nSaisie pour l'étudiant {i + 1}:")
    nom = input("Nom de l'étudiant : ")
    
    # Contrôle de saisie pour la note
    while True:
        try:
            note = float(input("Note de l'étudiant (entre 0 et 20) : "))
            if 0 <= note <= 20:
                break
            else:
                print("La note doit être comprise entre 0 et 20.")
        except ValueError:
            print("Veuillez entrer une valeur numérique valide pour la note.")

    # Ajouter les informations de l'étudiant dans la liste
    etudiants.append({"nom": nom, "note": note})

# Afficher les noms des étudiants ayant obtenu une note supérieure ou égale à 10
print("\nRésultat attendu :")
for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(f"{etudiant['nom']} a obtenu une note de {etudiant['note']}.")
