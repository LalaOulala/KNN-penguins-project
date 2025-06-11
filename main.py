import pandas, random # type: ignore
import new_penguins, visualisation

df = pandas.read_csv("penguins_size.csv")

df = df.rename(columns = {"species":"espèces", "island":"ile",
                          "culmen_length_mm":"longueur_bec","culmen_depth_mm":"profondeur_bec",
                          "flipper_length_mm":"longueur_nageoire","body_mass_g":"poids","sex":"sexe"})
df = df.dropna()
df.to_csv("penguins_size.csv", index=False)

# On ajoute un pingouin inconnu avec des caractéristiques aléatoires
# dans un nouveau fichier penguins_inconnu.csv
new_penguins.ajouter_pengouin_aleatoire(df)

# On affiche la caractéristique longueur_nageoire en fonction de l'individu
# renvoi un fichier select_caract_datas.csv
visualisation.select_caract("penguins_inconnu.csv", "longueur_bec", "x_longueur.csv")
visualisation.select_caract("penguins_inconnu.csv", "profondeur_bec", "y_profondeur.csv")

# On lit les valeurs des colonnes extraites dans les fichiers correspondants
df_longueur = pandas.read_csv("x_longueur.csv")
df_profondeur = pandas.read_csv("y_profondeur.csv")

# On affiche le graphique en deux dimensions avec les bonnes valeurs
visualisation.visualisation(df_longueur, df_profondeur, "y", "largueur_bec", "profondeur_bec")

