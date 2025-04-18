import random

def lancer_de(nombre_faces):
    return random.randint(1, nombre_faces) 


try:
    nombre_faces = int(input("Entrez le nombre de faces du dés : "))
    if nombre_faces <= 0:
        print("Le nombre de faces doit être supérieur à 0.")
    else:
        resultat = lancer_de(nombre_faces)
        print(f"Vous avez lancé un dé à {nombre_faces} faces et obtenu : {resultat}")
except ValueError:
    print("Veuillez entrer un nombre entier valide.") 


    