mot_de_passe = input("Entrez votre mot de passe : ")

if len(mot_de_passe) < 6:
    print("mot de passe trop court ")
elif mot_de_passe == '123456':
    print("mot de passe est bon")
else:
    print("Le mot de passe est incorrect")

print("Fin du programme")
