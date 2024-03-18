def verifier_age(age):

    try:
        age = int(age)  
        if age >= 18:
            print("Vous êtes un adulte mais votre sexe n'est pas clair.")
        elif age >= 0:
            print("Je peux voir vos cartes ?")
        else:
            print("Erreur : Tu peux pas avoir un age negatif, c'est illegal !")
    except ValueError:
        print("Erreur : Arretes de niaiser pis entres une valeur qui fait du sens saperlipopette !")


age_utilisateur = input("Tu veux acheter des cigarettes ? Mais t'as quel age au fait ? : ")
verifier_age(age_utilisateur)