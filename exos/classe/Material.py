class Material:
    """
    Classe représentant un matériel avec un nom et un numéro de série.
    """

    def __init__(self, nom, numeroSerie):
        """
        Initialise une instance de la classe Material avec un nom et un numéro de série.
        """
        self.nom = nom
        self.numeroSerie = numeroSerie
    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant l'objet de la classe Clavier.
        """
        return "Material : {} [{}]".format(self.nom, self.numeroSerie)