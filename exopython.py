import re #Importer le module pour les expressions régulier 

#Fonction pour vérifier si une chaîne de caractères est un nombre 

def valider_email(email):
    # Définir le modèle d'une adresse e-mail 

modele = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
return re.match(modele, email) is not None 

# Demander une adresse e-mail à l'utilisateur 

email = input("Entrez une adresse e-mail : ")

# Vérifier si l'adresse e-mail est valide 

if valider_email(email):
    print(f"L'adresse e-mail '{email}' est valide.")
else:
    print(f"L'adresse e-mail '{email}' n'est pas valide.")