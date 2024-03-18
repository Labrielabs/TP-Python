noms = ["Alice", "Bob", "Charlie", "David", "Eve"]
ages = [25, 30, 22, 28, 35]

personnes = dict(zip(noms, ages))

print("Le dictionnaire personnes est :", personnes)

while True:
    try:
        nouveau_nom = str(input("Entrez le nom de la nouvelle personne : "))
        nouvel_age = int(input("Entrez l'âge de la nouvelle personne : "))
        break
    except ValueError:
        print("L'âge doit être un nombre entier et le nom ne doit pas comporter de chiffres. Réessayez.")

personnes[nouveau_nom] = nouvel_age

print("Le dictionnaire personnes après l'ajout est :", personnes)
