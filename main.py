import pandas, random # type: ignore
import new_penguins, visualisation

df = pandas.read_csv("penguins_size.csv")

df = df.rename(columns = {"species":"espèces", "island":"ile",
                          "culmen_length_mm":"longueur_bec","culmen_depth_mm":"profondeur_bec",
                          "flipper_length_mm":"longueur_nageoire","body_mass_g":"poids","sex":"sexe"})
df = df.dropna()
df.to_csv("penguins_size.csv", index=False)

# On ajoute un pingouin inconnu avec des caractéristiques aléatoires
# dans un nouveau fichier unknown_penguins.csv
new_penguins.ajouter_pengouin_aleatoire(df)

# On affiche la profondeur_bec en fonction de la longueur_bec pour Adelie
fichier_source_affichage = "unknown_penguins.csv"
visualisation.select_caract(fichier_source_affichage, "espèces", "adelie_datas.csv", "Adelie")
visualisation.select_caract("adelie_datas.csv", "longueur_bec", "x_longueur_bec.csv")
visualisation.select_caract("adelie_datas.csv", "profondeur_bec", "y_profondeur_bec.csv")
# On affiche les données sélectionnées
df_x = pandas.read_csv("x_longueur_bec.csv")
df_y = pandas.read_csv("y_profondeur_bec.csv")
visualisation.visualisation(df_x, df_y, "r", "profondeur_bec", "longueur_bec")






