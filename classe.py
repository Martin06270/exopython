class Pizza:
    def __init__(self, base, prix, ingredients, diametre, style):
        self.base = base
        self.prix = prix
        self.ingredients = ingredients
        self.diametre = diametre
        self.style = style
    

    def ajouter_ingredients(self, nouvel_ingredient):
        if nouvel_ingredient == "ananas":
            raise TypeError("Les ananas ne sont pas acceptés sur cette pizza.")
        self.ingredients.append(nouvel_ingredient)
        self.prix = self.prix + 1

    def servir(self, table):
        print("J'amène la pizza à la table", table)

    def livre(self, adresse):
        print("Je livre la pizza à l'adresse :", adresse)

    base = input ("Entrez la base de la pizza : 
    prix = input ("Entrez le prix de la pizza : ")
    ingredients = input ("Entrez les ingrédients de la pizza : ")   
    diametre = input ("Entrez le diamètre de la pizza : ")
    style = input ("Entrez le style de la pizza : ")
    pizza = Pizza(base, prix, ingredients, diametre, style)