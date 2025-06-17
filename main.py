import pandas, random # type: ignore
import matplotlib.pyplot as plt # type: ignore
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

fichier_source_affichage = "fichiers_csv/unknown_penguins.csv"

# les différentes caractéristiques -> longueur_bec, profondeur_bec, longueur_nageoire, poids
caract_1 = "longueur_nageoire"
caract_2 = "longueur_bec"

# On affiche la profondeur_bec en fonction de la longueur_bec pour Adelie
visualisation.select_caract(fichier_source_affichage, "espèces", "fichiers_csv/adelie_datas.csv", "Adelie")
visualisation.select_caract("fichiers_csv/adelie_datas.csv", caract_1, "fichiers_csv/adelie_x_" + caract_1 + ".csv")
visualisation.select_caract("fichiers_csv/adelie_datas.csv", caract_2, "fichiers_csv/adelie_y_" + caract_2 + ".csv")

# Même chose pour Chinstrap
visualisation.select_caract(fichier_source_affichage, "espèces", "fichiers_csv/adelie_datas.csv", "Chinstrap")
visualisation.select_caract("fichiers_csv/adelie_datas.csv", caract_1, "fichiers_csv/chinstrap_x_" + caract_1 + ".csv")
visualisation.select_caract("fichiers_csv/adelie_datas.csv", caract_2, "fichiers_csv/chinstrap_y_" + caract_2 + ".csv")

# Pour Gentoo
visualisation.select_caract(fichier_source_affichage, "espèces", "fichiers_csv/adelie_datas.csv", "Gentoo")
visualisation.select_caract("fichiers_csv/adelie_datas.csv", caract_1, "fichiers_csv/gentoo_x_" + caract_1 + ".csv")
visualisation.select_caract("fichiers_csv/adelie_datas.csv", caract_2, "fichiers_csv/gentoo_y_" + caract_2 + ".csv")

# Pour le pingouin inconnu
visualisation.select_caract(fichier_source_affichage, "espèces", "fichiers_csv/adelie_datas.csv", "Inconnu")
visualisation.select_caract("fichiers_csv/adelie_datas.csv", caract_1, "fichiers_csv/inconnu_x_" + caract_1 + ".csv")
visualisation.select_caract("fichiers_csv/adelie_datas.csv", caract_2, "fichiers_csv/inconnu_y_" + caract_2 + ".csv")

# On affiche les données sélectionnées
df_x_1 = pandas.read_csv("fichiers_csv/adelie_x_" + caract_1 + ".csv")
df_y_1 = pandas.read_csv("fichiers_csv/adelie_y_" + caract_2 + ".csv")
df_x_2 = pandas.read_csv("fichiers_csv/chinstrap_x_" + caract_1 + ".csv")
df_y_2 = pandas.read_csv("fichiers_csv/chinstrap_y_" + caract_2 + ".csv")
df_x_3 = pandas.read_csv("fichiers_csv/gentoo_x_" + caract_1 + ".csv")
df_y_3 = pandas.read_csv("fichiers_csv/gentoo_y_" + caract_2 + ".csv")
df_x_4 = pandas.read_csv("fichiers_csv/inconnu_x_" + caract_1 + ".csv")
df_y_4 = pandas.read_csv("fichiers_csv/inconnu_y_" + caract_2 + ".csv")

# Construction de la figure
visualisation.visualisation(df_x_1, df_y_1, "r", caract_1, caract_2)
visualisation.visualisation(df_x_2, df_y_2, "b", caract_1, caract_2)
visualisation.visualisation(df_x_3, df_y_3, "y", caract_1, caract_2)
visualisation.visualisation(df_x_4, df_y_4, "black", caract_1, caract_2)

plt.legend(["Adélie", "Chinstrap", "Gentoo", "Inconnu"])
plt.show()






