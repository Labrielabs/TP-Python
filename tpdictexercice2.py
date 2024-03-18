personne = {
    "nom": "Stéphane",
    "âge": 38,
    "ville": "Terrebonne"
}

print(f"L'âge de la personne est : {personne['âge']} ans")

personne["ville"] = "Paris"

personne["sexe"] = "Masculin"

del personne["ville"]

print("Le dictionnaire résultant est :", personne)

