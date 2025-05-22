import folium 

carte = folium.Map(location=[48.8566,2.3522], zoom_start=13)

# Ajout d'un marqueur
lieux = [
    {"nom":"Tour Eiffel","coords": [48.8588443, 2.2943506], "thématique":"Monument","description":"Symbole de Paris"}
    ,{"nom":"Louvre","coords": [48.8606111, 2.337677], "thématique":"Musée","description":"Le plus grand musée du monde "}
    ,{"nom":"Notre-Dame","coords": [48.85296819999999, 2.3499021], "thématique":"Monument","description":"Cathédrale emblématique de Paris"}
    ,{"nom":"Montmartre","coords": [48.8867, 2.3431], "thématique":"Quartier","description":"Quartier artistique de Paris"}
    ,{"nom":"Le Marais","coords": [48.8559, 2.3623], "thématique":"Quartier","description":"Quartier historique de Paris"}
    ,{"nom":"Musée d'Orsay","coords": [48.8601, 2.3266], "thématique":"Musée","description":"Musée d'art impressionniste"}
    ,{"nom":"Sainte-Chapelle","coords": [48.8554, 2.3441], "thématique":"Monument","description":"Chapelle gothique célèbre"}
    ,{"nom":"Centre Pompidou","coords": [48.8606, 2.3522], "thématique":"Musée","description":"Musée d'art moderne et contemporain"}
    ,{"nom":"Quartier Latin","coords": [48.8431, 2.3444], "thématique":"Quartier","description":"Quartier étudiant et historique"}
    ,{"nom":"Palais Garnier","coords": [48.8719, 2.3314], "thématique":"Monument","description":"Opéra de Paris"}
    ,{"nom":"Champs-Élysées","coords": [48.8698, 2.3073], "thématique":"Quartier","description":"Avenue emblématique de Paris"}
    ,{"nom":"Arc de Triomphe","coords": [48.8738, 2.2950], "thématique":"Monument","description":"Monument commémoratif"}
    ,{"nom":"Musée Picasso","coords": [48.8610, 2.3622], "thématique":"Musée","description":"Musée dédié à l'artiste Pablo Picasso"}    
    

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
