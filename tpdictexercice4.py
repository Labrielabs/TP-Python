# Créer une liste de dictionnaires représentant des étudiants
etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob", "note": 8},
    {"nom": "Charlie", "note": 12},
    {"nom": "David", "note": 18},
    {"nom": "Eve", "note": 9}
]

# Afficher les noms des étudiants ayant obtenu une note supérieure ou égale à 10
for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(f"{etudiant['nom']} a obtenu une note de {etudiant['note']}.")

# Résultat attendu :
# Alice a obtenu une note de 15.
# Charlie a obtenu une note de 12.
# David a obtenu une note de 18.
