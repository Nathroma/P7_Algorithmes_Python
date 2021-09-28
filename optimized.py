import sys
import csv
import time

from math import ceil

start_time = time.time()

prix_max = 500

def somme(list):
    somme = []
    for action in list:
        somme.append(action[1])
    return (sum(somme))


def knapsack(list):

    price = prix_max*10

    matrice = [[0 for x in range(price + 1)] for x in range(len(list) + 1)]

    for action in range(1, len(list) + 1):
        for cout in range(1, price + 1):
            if list[action-1][1] <= cout:
                matrice[action][cout] = max(
                    list[action-1][2] + matrice[action-1][cout-list[action-1][1]],
                    matrice[action-1][cout]
                )
            else:
                matrice[action][cout] = matrice[action-1][cout]

    nb_actions = len(list)
    combinaisons = []

    while price >= 0 and nb_actions >= 0:
        i = list[nb_actions-1]
        if matrice[nb_actions][price] == matrice[nb_actions-1][price-i[1]] + i[2]:
            combinaisons.append(i)
            price -= i[1]

        nb_actions -= 1

    print("Meilleurs résultats : ")
    for combinaison in combinaisons:
        print(combinaison[0])
    print("Nombre d'actions retenu : ", len(combinaisons))
    print("Prix : ~", somme(combinaisons)/10, "€")
    print("Bénéfice en deux ans : ", matrice[-1][-1], "€")
    print("temps d'exécution : ", time.time() - start_time, "secondes")



try:
    with open(sys.argv[1], newline='') as csvfile:
        actions = csv.reader(csvfile, delimiter=',', quotechar='|')
        list_actions = []
        for case in actions:
            if float(case[1]) <= 0:
                pass
            else:
                list_actions.append(
                    [case[0],int(ceil(float(case[1])*10)),float(float(case[1]) * float(case[2].replace('%', '')) / 100),])

        knapsack(list_actions)
    

# Dans le cas ou le fichier n'existe pas 
except FileNotFoundError:
    print("Le fichier demandé est introuvable, veuillez vérifier le nom")