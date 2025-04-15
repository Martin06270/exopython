moyenne = input("Entrez votre moyenne générale : ")

if len(moyenne):
    try:
        moyenne = float(moyenne)  # Convertit en nombre

        if moyenne >= 18:
            print("Félicitations")
        elif moyenne >= 16:
            print("Très bien")
        elif moyenne >= 14:
            print("Bien")
        elif moyenne >= 12:
            print("Assez bien")
        else:
            print("Insuffisant")

    except ValueError:
        print("Veuillez entrer un nombre valide.")
else:
    print("Veuillez entrer un nombre .") 