import pandas, os # type: ignore
import matplotlib.pyplot as plt # type: ignore

def select_caract(datas, colonne, file_name="fichiers_csv/select_caract_datas.csv", valeur=""):
    """
    Extrait toutes les lignes ayant une certaine valeur dans une colonne donnée.
    Si la valeur n'est pas renseignée, la fonction extrait simplement toute la colonne (par défaut si valeur non renseignée).
    Elle renvoie la DataFrame ainsi générée dans un fichier csv.


    Args:
        datas (string): le chemin du fichier .csv à traiter.
        colonne (string): le nom de la colonne concernée.
        valeur (string): la valeur à rechercher dans la colonne pour filtrer les lignes (laisser vide pour ne pas filtrer).
        file_name (string): le nom du fichier .csv de sortie.

    Returns:
        None. Crée un fichier CSV contenant les lignes ou la colonne extraite selon les critères.
    """

    if valeur == "":
        df = pandas.read_csv(datas)
        df1 = df[colonne]
        df1.to_csv(file_name, index=False)
    
    else:
        df = pandas.read_csv(datas)
        df1 = df[df[colonne] == valeur]
        df1.to_csv(file_name, index=False)


def supprimer_fichier(chemins):
    """
    Supprime le fichier si il existe, sinon affiche un message.

    Args:
        chemin (list): liste contenant les chemins des fichier que l'on veut supprimer

    Returns:
        None. Supprime un fichier
    """
    for chemin in chemins:
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