import pandas, random # type: ignore

def ajouter_pengouin_aleatoire(df):
    """Ajoute un pengouin avec des caractéristiques aléatoires à la fin
    du fichier csv penguins_size.csv et renvoie un dictionnaire ayant pour clé
    les descripteurs des données et pour valeurs les caractéristiques du pingouin
    inconnu

    Args:
        df (DataFrame): les données lu dans le fichier penguins_size.csv
    Returns:
        inconnu (dict): dictionnaire ayant pour clé les descripteurs
        des données et pour valeurs les caractéristiques du pingouin inconnu
    """

    # On détermine les intervalles de valeurs pour chaque colonne numérique
    intervalles_valeurs = {} # On les range dans un dictionnaire
    colonnes_numeriques = ["longueur_bec", "profondeur_bec", "longueur_nageoire", "poids"]
    for colonne in colonnes_numeriques:
        valeur_max = df[colonne].max() # valeur maximum de chaque colonne numérique
        valeur_min = df[colonne].min() # valeur minimum de chaque colonne numérique
        intervalles_valeurs[colonne] = [valeur_min, valeur_max]

    # On créé un nouveau pinguin inconnu
    inconnu = {"Unnamed: 0":df["Unnamed: 0"].max() + 1,"espèces":"Inconnu", "ile":"Inconnu"} # ce qu'on va chercher à déterminer avec le KNN
    for descripteur in intervalles_valeurs: # des valeurs aléatoires dans les bons intervalles
        intervalle = intervalles_valeurs[descripteur]
        inconnu[descripteur] = round(random.uniform(intervalle[0], intervalle[1]), 1) # arrondi au dixième
    inconnu["sexe"] = random.choice(["FEMALE", "MALE"]) # un sexe aléatoire

    # On crée un nouveau fichier .cvs qui est une copie de penguins_size mais avec le pingouin inconnu
    df_inconnu = pandas.DataFrame(inconnu, index=[len(df) + 1])
    df2 = pandas.concat([df, df_inconnu])
    df2.to_csv("unknown_penguins.csv", index=False)

    return inconnu
