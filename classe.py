class Pizza:
    def __init__(self, base, prix, ingredients, diametre, style):
        self.base = base
        self.prix = prix
        self.ingredients = ingredients
        self.diametre = diametre
        self.style = style
    

    def ajouter_ingredients(self, nouvel_ingredient):
        if nouvel_ingredient == "ananas":
            
