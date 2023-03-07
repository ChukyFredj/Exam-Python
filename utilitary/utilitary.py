# Fonction de choix pour continuer ou pas à faire des exercices
def choice_():
    print("\n\nVoulez-vous essayer un autre exercice ? (O / N)\n> ", end="")
    while True:
        test = input()
        if test in ("O","o"):
            return True
        elif test in ("N","n"):
            return False
        else:
            print("Choisissez une réponse valide !")

# Fonction pour choisir un nombre positif avec une gestion d'erreur commune a plein d'exos
def verif_1error(txt,minval=0):
    test: int
    toReturn: int
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = int(number)
            if minval:
                print("Vous devez choisir un nombre positif !")
                continue
            break
        except ValueError:
            print("Vous devez choisir un nombre positif !")
    return test
