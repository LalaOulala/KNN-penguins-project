import pandas, os # type: ignore
import matplotlib.pyplot as plt # type: ignore

def select_caract(datas, colonne, file_name="select_caract_datas.csv"):
    """À partir d'une table de données et du nom d'une colonne dans cette table,
    on renvoie une nouvelle table qui contient toutes les lignes de la table originale
    mais seulement la colonne donnée en argument.

    Args:
        datas (string): le chemin du fichier .csv que l'on souhaite utiliser comme donnée d'entrée
        colonne (string): le nom de la colonne que l'on souhaite extraire
        file_name (string): le nom du fichier .csv créé

    Returns:
        None. Crée un fichier .csv nommé file_name
    """

    df = pandas.read_csv(datas)
    df1 = df[colonne]
    df1.to_csv(file_name, index=False)


def supprimer_fichier(chemin):
    """Supprime le fichier si il existe, sinon affiche un message.

    Args:
        chemin (string): chemin d'un fichier que l'on veut supprimer

    Returns:
        None. Supprime un fichier
    """
    if os.path.isfile(chemin):
        os.remove(chemin)
        print(f"Fichier supprimé : {chemin}")
    else:
        print(f"Fichier non trouvé : {chemin}")


def visualisation(x, y, color, xlabel="abscisse", ylabel="ordonné"):
    """
    Affiche un nuage de points (scatter plot) en deux dimensions à partir des coordonnées x et y,
    avec une légende indiquant les catégories associées.

    Args:
        x (list): Les valeurs à placer sur l'axe des abscisses.
        y (list): Les valeurs à placer sur l'axe des ordonnées.
        color (string): La couleur d'affichage des points.
        xlabel (string): nom donné à l'axe des abscisses dans notre graphe (par défaut -> "abscisse")
        ylabel (string): nom donné à l'axe des ordonnées dans notre graphe (par défaut -> "ordonnée")

    Returns:
        None. Affiche un graphique matplotlib.
    """
    plt.scatter(x, y, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


