nombres = [1, 2, 3, 4, 5]

nombres.extend([6, 7, 8, 9, 10])

longueur_liste = len(nombres)
print(f"La longueur de la liste est : {longueur_liste}")

nombres.remove(3)

nombres.sort(reverse=True)

print("La liste triée dans l'ordre décroissant est :", nombres)

