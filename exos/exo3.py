from exos.classe.Material import Material
from exos.classe.Clavier import Clavier
from exos.classe.Ecran import Ecran
def exo_3():
    """
    Script permettant de compter le nombre de mots dans une chaine de caractères
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        print("---------------Exemple----------------------")
        mat = Material("TypeEcran", "E123456789")
        print(mat)
        print(mat.numeroSerie, mat.nom)
        print("--------------------------------------------")
        print("---------------Exemple----------------------")
        c = Clavier("TypeEcran","E123456789", 102)
        print(c)
        print(c.numeroSerie, c.nom, c.nbTouche)
        print("--------------------------------------------")
        print("---------------Exemple----------------------")
        e = Ecran("LD","E123456789", "1024x768")
        print(e)
        print(e.numeroSerie, c.nom, e.taille)
        print("--------------------------------------------")
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break