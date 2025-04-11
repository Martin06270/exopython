from datetime import datetime, timedelta # Importing datetime and timedelta from datetime module

# Afficher l'heure actuelle 

heure_actuelle = datetime.now()
print(f"Heure actuelle : {heure_actuelle.strftime('%H:%M:%S')}")

# Demander à l'utilisateur combien d'heures ajouter
heures_a_ajouter = int(input("Entrez le nombre d'heures à ajouter : "))

# Calculer l'heure future
heure_future = heure_actuelle + timedelta(hours=heures_a_ajouter)
print(f"Dans {heures_a_ajouter} heure(s), il sera : {heure_future.strftime('%H:%M:%S')}")

