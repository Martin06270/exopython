import folium 

carte = folium.Map(location=[48.8566,2.3522], zoom_start=13)

# Ajout d'un marqueur
lieux = [
    {"nom":"Tour Eiffel","coords": [48.8588443, 2.2943506], "thématique":"Monument","description":"Symbole de Paris"}
    ,{"nom":"Louvre","coords": [48.8606111, 2.337677], "thématique":"Musée","description":"Le plus grand musée du monde "}
    ,{"nom":"Notre-Dame","coords": [48.85296819999999, 2.3499021], "thématique":"Monument","description":"Cathédrale emblématique de Paris"}
    ,{"nom":"Montmartre","coords": [48.8867, 2.3431], "thématique":"Quartier","description":"Quartier artistique de Paris"}

]


#Couleurs icones par thématique 

styles = {
    "Monument":{"color":"red", "icon":"home"},
    "Musée":{"color":"blue", "icon":"book"},
    "Quartier":{"color":"green", "icon":"tree-deciduous"},
}


# Ajouter chaque point à la carte 

for lieu in lieux:
    folium.Marker(
        location=lieu["coords"],
        popun=f"{lieu['nom']}</b><br>{lieu['description']}</b><br>{lieu['thématique']}",
        tooltip=lieu["nom"],
        icon=folium.Icon(
            color=styles[lieu["thématique"]]["color"],
            icon=styles[lieu["thématique"]]["icon"],
            prefix="glyphicon"  # Prefix pour les icons Bootstrap
        )
    ).add_to(carte) #Pour ajouter le marqueur à la carte 

#Sauvegarde de la carte 
carte.save("carte_interactive.html")
print("Carte générée avec Sucés! Ouvrez le fichier 'carte_interactive.html'")
