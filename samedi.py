# Partie 1 : Vérifier si l'utilisateur est majeur en fonction de son année de naissance
année_naissance = int(input("Veuillez saisir votre année de naissance : "))

âge = 2024 - année_naissance  # Supposons que l'année actuelle est 2024

if âge >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")

# Partie 2 : Vérifier si l'utilisateur est majeur ou mineur en fonction de son âge
âge = int(input("Veuillez saisir votre âge : "))

if âge >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")

# Partie 3 : Déterminer la parité d'un nombre entier saisi par l'utilisateur
nombre = int(input("Veuillez saisir un nombre entier : "))

if nombre % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")