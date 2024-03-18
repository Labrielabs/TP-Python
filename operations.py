# operations.py

def addition(a, b):
    """
    Calcule la somme de deux nombres entiers.
    :param a: Premier nombre entier
    :param b: Deuxième nombre entier
    :return: Somme des deux nombres
    """
    try:
        a = int(a)
        b = int(b)
        return a + b
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides.")
        return None

def multiplication(a, b):
    """
    Calcule le produit de deux nombres entiers.
    :param a: Premier nombre entier
    :param b: Deuxième nombre entier
    :return: Produit des deux nombres
    """
    try:
        a = int(a)
        b = int(b)
        return a * b
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides.")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    num1 = input("Entrez le premier nombre : ")
    num2 = input("Entrez le deuxième nombre : ")

    # Appel des fonctions
    somme = addition(num1, num2)
    produit = multiplication(num1, num2)

    if somme is not None:
        print(f"La somme de {num1} et {num2} est : {somme}")
    if produit is not None:
        print(f"Le produit de {num1} et {num2} est : {produit}")
