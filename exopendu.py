nb_vies = 7

mot_mystere = 'python'

mot_public = '_' * len(mot_mystere)

while nb_vies > 0 and mot_public != mot_mystere:

    lettre =input('Entrez une lettre :  ')

    if lettre in mot_mystere:
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i+1:]
            else:
                nb_vies -= 1

if mot_public == mot_mystere:

    print('Bravo vous avez gagné ! Le mot était :', mot_mystere)

if nb_vies == 0:
    print ('Dommage vous avez perdu ! Le mot était :', mot_mystere)

else:
    print ('Vous avez ' , nb_vies, 'vies restantes ')

    print ('le mot mystère était :', mot_mystere)
    

