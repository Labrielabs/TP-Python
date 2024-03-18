# nouveaufichierpython.py
"""
Importez le module operations créé dans l'exercice précédent dans un nouveau fichier Python.

Utilisez les fonctions addition et multiplication du module importé pour effectuer des opérations 
arithmétiques avec des nombres saisis par l'utilisateur.

"""
import operations

def get_user_input():
    try:
        num1 = int(input("Entrez le premier nombre : "))
        num2 = int(input("Entrez le deuxième nombre : "))
        return num1, num2
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides.")
        return None, None

num1, num2 = get_user_input()

if num1 is not None and num2 is not None:
    somme = operations.addition(num1, num2)
    produit = operations.multiplication(num1, num2)

    if somme is not None:
        print(f"La somme de {num1} et {num2} est : {somme}")
    if produit is not None:
        print(f"Le produit de {num1} et {num2} est : {produit}")
