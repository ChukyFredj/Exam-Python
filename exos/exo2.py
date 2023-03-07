from utilitary import *

def suite(A, B, N):
    """
    Calcule les termes de la suite U_n = (U_{n-1} + U_{n-2}) / 2 avec U_0 = A et U_1 = B,
    jusqu'à atteindre la valeur N > 0.
    """
    assert A > 0 and B > 0, "Les valeurs de A et B doivent être strictement positives."
    assert N > 0, "La valeur de N doit être strictement positive."
    Un_1 = A
    Un = B
    for n in range(2, N+1):
        Un, Un_1 = (Un + Un_1) / 2.0, 2/(1/Un_1 + 1/Un)
    return Un, Un_1



def Exercice2():
    """
    Teste la fonction suite() en comparant les résultats avec les valeurs attendues.
    """
    
    while True:
        tests = [{"A": 1, "B": 1, "N": 10}, {"A": 1, "B": 2, "N": 10}, {"A": 1, "B": 3, "N": 10}, {"A": 1, "B": 1, "N": 10}]
        for test in tests:
            A, B, N = test["A"], test["B"], test["N"]
            U, U_1 = suite(A, B, N)
            print("a={} b={} N={} => suite = ({}, {})".format(A, B, N, U, U_1))
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break
    

