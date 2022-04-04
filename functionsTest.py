import csv
import concurrent.futures
import os
import genericpath
import time


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = lst[:middle]
    # print("left" + str(left))
    right = lst[middle:]
    # print("right" + str(right))
    sleft = merge_sort(left)
    sright = merge_sort(right)
    return merge_list(sleft, sright)


def merge_list(left, right):
    result = []
    while (left and right):
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


def round_float(arg):
    return round(float(arg), 2)

#true
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][int(w - wt[i - 1])],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


def knapSackList(W, liste, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif liste[i - 1][1] <= w:
                K[i][w] = max(liste[i - 1][-1]
                              + K[i - 1][int(w - liste[i - 1][1])],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


# version liste
# def knapSackList(W, liste, n):
#     if n == 0 or W == 0:
#         return 0,""
#     if (liste[n-1][1] > W):
#         return knapSackList(W, liste, n-1)
#     else:
#         # print(liste[n-1][2])
#         knapSack1 = knapSackList(W-liste[n-1][1], liste, n-1)
#         knapSack2 = knapSackList(W, liste, n-1)
#         if liste[n-1][-1] + knapSack1[0] > knapSack2[0]:
#             return (liste[n-1][-1] + knapSack1[0], str(liste[n-1][0] + ", "+knapSack1[1]))
#         return knapSack2


def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield [elements[i],]
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield [elements[i],] + next


def csv_read_threaded(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        header = next(spamreader)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            list_csv = list(executor.map(lambda x: benefit_row_calculator(x), spamreader))
    return list_csv


def benefit_row_calculator(row):
    row_calculated = [row[0], float(row[1]), float(row[2])] + [round(float((float(row[1]) * float(row[2]) / 100)), 2)]
    return row_calculated

def creation_dossier_categorie(rows_list):
    cwd = os.getcwd()
    directory = cwd + '/'
    nom_csv = 'test5.csv'
    path = directory + nom_csv
    EN_TETE_COLONNES = ["n", "temps", "gain"]
    with open(os.path.join(directory + nom_csv), 'w', newline="", encoding="utf-8-sig") as csv_file:
        ligneXcel = csv.writer(csv_file, delimiter=',')
        ligneXcel.writerow(EN_TETE_COLONNES)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            csv_rows = list(executor.map(lambda x: ligneXcel.writerow(x), rows_list))
    return path

def rows_list(W, list_test, n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tables = list(executor.map(lambda x: boucle(W, list_test, x), range(n)))
    return tables



def boucle(W, list_test, i):
    start = time.time()
    result_minus = knapSackList(W, list_test, i)
    end = time.time()
    timing = end - start
    row = [i, timing, round_float(result_minus)]
    return row