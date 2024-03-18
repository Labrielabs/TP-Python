def est_present(ma_liste, valeur):
    
    return valeur in ma_liste

# Exemple d'utilisation
ma_liste = [10, 20, 30, 40, 50]
valeur_recherchee = 30


def creer_liste(taille):
     
ma_liste = []
for i in range(taille):
        element = input(f"Entrez l'élément {i+1} : ")
        ma_liste.append(element)
    
    return ma_liste




if est_present(ma_liste, valeur_recherchee):
    print(f"La valeur {valeur_recherchee} est présente dans la liste.")
else:
    print(f"La valeur {valeur_recherchee} n'est pas dans la liste.")
