try:
        nombre = int(nombre)  # Convertir l'entrée en entier
        if nombre % 2 == 0:
            return True
        else:
            return False
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
        return False