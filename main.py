import pandas, random # type: ignore
import new_penguins

df = pandas.read_csv("penguins_size.csv")

df = df.rename(columns = {"species":"espèces", "island":"ile",
                          "culmen_length_mm":"longueur_bec","culmen_depth_mm":"profondeur_bec",
                          "flipper_length_mm":"longueur_nageoire","body_mass_g":"poids","sex":"sexe"})
df = df.dropna()
df.to_csv("penguins_size.csv", index=False)

# On ajoute un pingouin inconnu avec des caractéristiques aléatoires
new_penguins.ajouter_pengouin_aleatoire(df)
