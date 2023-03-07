from exos.classe.Material import Material
class Clavier(Material):
    """
    Classe représentant un clavier qui hérite de la classe Material et ajoute un attribut nbTouche.
    """

    def __init__(self, nom, num_serie, nbTouche):
        """
        Initialise une instance de la classe Clavier avec un nom, un numéro de série et un nombre de touches.
        """
        super().__init__(nom, num_serie)
        self.nbTouche = nbTouche
    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant l'objet de la classe Clavier.
        """
        return "Material :Clavier [{}]\n* NbTouche {}".format(self.numeroSerie, self.nbTouche)