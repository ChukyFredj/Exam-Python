def seuil(P, T):
    N = 1
    print("|     P    |    N    |")
    while P < 1000:
        P *= T
        if (P > 1000):
            return N - 1
        else :
            print("|    {:.2f}|        {}|".format(P, N))
            N += 1
    return N


def exercice1():
    """
    Script permettant de rentrer une chaine de caractères et d'inverser une chaine de caractères
    """

    while True:
        # Définition de la fonction à intégrer
        # Saisie des variables
        P = float(input("Rentrer P > "))
        T = float(input("Rentrer T > "))
        N = seuil(P, T)
        print("Nmax : ", N)
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break
