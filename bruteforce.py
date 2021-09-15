"""
    Programme bruteforce.py pour résoudre un probleme de calcul avec une fonction recursive
"""
from itertools import combinations

import time
import csv
import sys

start_time = time.time()

max_cost = 500


def combinaisons(actions_list):
    # Creation de la variable pour tri des combinaisons
    best_actual = 0

    # Creation des differentes combinaisons possibles
    for i in range(len(actions_list)):
        combinaisons = combinations(actions_list, i + 1)

    # Pour chaque combinaison, calculer le prix total des actions
        for combinaison in combinaisons:
            prices = action_price(combinaison)

    # Verifier si son prix n'excede pas la valeur max d'achat (500€)
            if prices <= max_cost:
                benefice_action = calcul_benefice(combinaison)

    # Vérifier chaque combinaison retenu pour ressortir celle 
    # avec le plus de benefices
                if benefice_action > best_actual:
                    best_actual = benefice_action
                    best_combi = combinaison


    # Affcihage des résultats dans le terminal
    print("Actions retenu pour achat : ")

    for comb in best_combi:
        print(comb)

    print('Temps de calcul : ', time.time() - start_time, "secondes")
    print('Cout total : ', action_price(best_combi), '€')
    print('Pour un benefice de : ', best_actual, '€ en 2 ans.')


# Ressort la somme des couts des actions pour la combinaison actuel
def action_price(list):
    prices = []
    for action in list:
        prices.append(action[1])
    return (sum(prices))


# Ressort la somme des bénéfices des actions pour la combinaison actuel
def calcul_benefice(list):
    calculs = []
    for action in list:
        calculs.append(action[1] * action[2] / 100)
    return (sum(calculs))

try:
    with open(sys.argv[1], newline='') as csvfile:
        actions = csv.reader(csvfile, delimiter=',', quotechar='|')
        list_actions = []
        for case in actions:
            list_actions.append([case[0], float(case[1]), float(case[2].replace('%', ''))])
        combinaisons(list_actions)
    
except FileNotFoundError:
    print("Le fichier demandé est introuvable, veuillez vérifier le nom")