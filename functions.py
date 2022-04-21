import csv
import concurrent.futures
import os
import time


# Arrondi à deux décimales
def round_float(arg):
    return round(float(arg), 2)


# Génération de liste pour l'algorithme de force brute
def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield [elements[i], ]
        else:
            for j in choose_iter(elements[i+1:len(elements)], length-1):
                yield [elements[i], ] + j


# 1 - Lecture du csv avec calcul du bénéfice
def csv_read_threaded(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            list_csv = list(executor.map(lambda x: benefit_row_calculator(x), spamreader))
    return list_csv


# Calcul du bénéfice
def benefit_row_calculator(row):
    row_calculated = [row[0], float(row[1]), float(row[2])] + [round(float((float(row[1]) * float(row[2]) / 100)), 2)]
    return row_calculated


# 2 - Nettoyage des actions à prix nul ou négatif
def value_cleaner(list_arg, x):
    if x[1] > 0:
        return list_arg.append(x)
    else:
        return 0


def threaded_clean_list(list_arg):
    list_clean = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        list(executor.map(lambda x: (value_cleaner(list_clean, x)), list_arg))
    return list_clean


# 3 - Merge sort
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]
    sleft = merge_sort(left)
    sright = merge_sort(right)
    return merge_list(sleft, sright)


def merge_list(left, right):
    result = []
    while left and right:
        if left[0][2] > right[0][2]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        result += right
    return result


# 4 - Algorithme du sac à dos
def knap_sack_list_name(w, list_arg, n):
    total_price = 0.0
    k = [[[0, ""] for x in range(w + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                k[i][j][0] = 0
                k[i][j][1] = ""
            elif list_arg[i - 1][1] <= j:
                knap_one = list_arg[i - 1][-1] + k[i - 1][int(j - list_arg[i - 1][1])][0]
                knap_two = k[i - 1][j][0]
                if knap_one > knap_two:
                    k[i][j][0] = knap_one
                    k[i][j][1] = list_arg[i - 1][0] + ", " + k[i - 1][int(j - list_arg[i - 1][1])][1]
                    total_price = w - list_arg[i - 1][1]
                else:
                    k[i][j][0] = knap_two
                    k[i][j][1] = k[i - 1][j][1]
            else:
                k[i][j][0] = k[i - 1][j][0]
                k[i][j][1] = k[i - 1][j][1]
    return total_price, round_float(k[n][w][0]), k[n][w][1]


# Précision
def precision_fold(list_arg, fold=1):
    list_arg[1] = list_arg[1]*fold
    return list_arg


# Fonction de print
def print_result(tuple_arg, timing, n, fold):
    cost = tuple_arg[0]/fold
    percent_profit = round_float(tuple_arg[1] / cost*100)
    share_list = tuple_arg[2].split(", ")
    share_list.pop()
    share_list.reverse()
    timing = round(timing, 4)
    check = round(timing / n, 4)
    print(f"""Algorithme terminé :
    Actions pertinentes étudiées : {n}
    Précision : {fold/100}/0.01
    Temps écoulé : {timing} secondes ({check}s/n)
    Coût total : {cost}
    Bénéfice : {tuple_arg[1]} ({percent_profit}% de profit)
    Actions sélectionnées : {share_list}""")
    # list(map(lambda x: print(x), share_list))


# Fonction d'algorithme complet
def complete_algorithm(w, list_arg, start_time,  fold=1):
    list_clean = threaded_clean_list(list_arg)
    list_clean = merge_sort(list_clean)
    n = len(list_clean)
    w = w * fold
    list_ten = list(map(lambda x: precision_fold(x, fold), list_clean))
    result_fast = knap_sack_list_name(w, list_ten, n)
    end = time.time()
    timing = end - start_time
    print_result(result_fast, timing, n, fold)
    return result_fast, timing


# Ecriture dans un csv
def creation_dossier_category(rows_list_arg,i=""):
    cwd = os.getcwd()
    directory = cwd + '/'
    nom_csv = "test_file1_"+i+".csv"
    path = directory + nom_csv
    header = ["n", "temps", "gain"]
    with open(os.path.join(directory + nom_csv), 'w', newline="", encoding="utf-8-sig") as csv_file:
        excel_row = csv.writer(csv_file, delimiter=',')
        excel_row.writerow(header)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            list(executor.map(lambda x: excel_row.writerow(x), rows_list_arg))
    return path


# Liste des lignes
def rows_list(w, list_test, n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tables = list(executor.map(lambda x: boucle(w, list_test, x), range(n)))
    return tables


# # Liste des lignes
# def rows_list_complete(w, list_test, n):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         tables = list(executor.map(lambda x: boucle_complete(tuple_return, timing), range(n)))
#     return tables


# Fonction boucle pour l'écriture dans un csv
def boucle(w, list_test, i):
    start = time.time()
    result_minus = knap_sack_list_name(w, list_test, i)
    end = time.time()
    timing = round(float(end - start), 6)
    nb_actions = int(len(result_minus[-1])/12)
    row = [i, timing, round_float(result_minus[1]), nb_actions]
    return row


# def boucle_complete(w, list_arg, start_time, fold = 1, i):
#     tuple_return = complete_algorithm(w, list_arg, start_time, fold)
#     row = [i, timing, tuple_return[1], tuple_return[0], len(tuple_return[-1])]
#     return row
