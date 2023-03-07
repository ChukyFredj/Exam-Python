from exos import *
from utilitary import *


# Fonction de lancement du menu pour le choix des exercices disponibles
def menu():
    while True:
        print("\n\nListe des exercices de L'examen disponibles (Taper le numéro de l'exercice) :\n")
        print("Exercice 1 >  ")
        print("Exercice 2 >  ")
        print("Exercice 3 >  ")
        print("0 > Quitter\n")
        choice = verif_1error("Choisissez l'exercice voulu : ")
        print("\n\n\n")
        match choice:
            case 0:
                print("Très bien, au revoir...")
                return
            case 1:
                exercice1()
            case 2:
                Exercice2()
            case 3:
                exo_3()
        if not choice_():
            print("Très bien, au revoir...")
            return
