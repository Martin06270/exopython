import random
# appdés.py - Un simple simulateur de lancer de dés

def lancer_de(nombre_faces):
    return random.randint(1, nombre_faces)
# Demande à l'utilisateur le nombre de faces du dé



try:
    nombre_faces = int(input("Entrez le nombre de faces du dés : "))
    # Vérifie que le nombre de faces est supérieur à 0
    # Si le nombre de faces est inférieur ou égal à 0, affiche un message d'erreur
    if nombre_faces <= 0:
        print("Le nombre de faces doit être supérieur à 0.")
    else:
        resultat = lancer_de(nombre_faces)
        print(f"Vous avez lancé un dé à {nombre_faces} faces et obtenu : {resultat}")
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
# Gère les erreurs de saisie



    