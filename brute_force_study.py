import time
import pandas as pd
import csv
import concurrent.futures

#Liste des actions
list_ = "Action-1:20:1;Action-2:30:3;Action-3:50:7,5;Action-4:70:14;Action-5:60:10,2;Action-6:80:20;Action-7:22:1,54;Action-8:26:2,86;Action-9:48:6,24;Action-10:34:9,18;Action-11:42:7,14;Action-12:110:9,9;Action-13:38:8,74;Action-14:14:0,14;Action-15:18:0,54;Action-16:8:0,64;Action-17:4:0,48;Action-18:10:1,4;Action-19:24:5,04;Action-20:114:20,52"

# Liste des noms des actions
listi = list(map(lambda x: x.split(":")[0], list_.split(";")))

# Créé un tuple (prix de l'action, bénéfice(valeur))
listy = {i.split(":")[0]: tuple(map(lambda x: round(float(x), 2), i.split(":")[1:])) for i in list_.replace(",", ".").split(";")}

# Liste des prix des actions
wt = list(map(lambda x: listy[x][0], listi))

# Liste des bénéfices des actions en valeur numéraire
val = list(map(lambda x: listy[x][1], listi))

def csv_read_threaded(file):
    """Read the selected cv file and return a list including a calculated benefit"""
    print(f"Reading {file}...")
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            list_csv = list(executor.map(lambda x: benefit_row_calculator(x), spamreader))
    return list_csv

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

# Calcul du bénéfice
def benefit_row_calculator(row):
    row_calculated = [row[0], float(row[1]), float(row[2])] + [round(float((float(row[1]) * float(row[2]) / 100)), 2)]
    return row_calculated


# Liste au format de la réponse finale ["Actions", coût total, bénéfice]
maxy = ["", 0, 0]
W = 500


def choose_iter(elements, length):
    """Fonction génératrice des itérateurs correspondants aux combinaisons possibles"""
    for i in range(len(elements)):
        if length == 1:
            yield [elements[i], ]
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield [elements[i], ] + next


file_two = "C:\opc finis\Projet 7\data\dataset2_Python+P7.csv"
list_start = csv_read_threaded(file_two)
list_clean = threaded_clean_list(list_start)

listi = []
listy = {}
for i in list_clean:
    listi.append(i[0])
    tuple_list = (int(i[1]), int(i[3]))
    listy[i[0]] = tuple_list

n = 29
study_list = []

# listy = {i.split(":")[0]: tuple(map(lambda x: round(float(x), 2), i.split(":")[1:])) for i in list_.replace(",", ".").split(";")}
print(listy)


# Algorithme de force brute
for j in range(26,n+1):
    start = time.time()
    for i in range(1, j):

        # Pour chaque combinaison, calcule le coût total et bénéfice
        s = list(map(lambda x: (x,
                                sum(map(lambda j: listy[j][0], x)),
                                round(float(sum(map(lambda k: listy[k][1], x))), 2)),
                     choose_iter(listi[:j], i)))
        # Retire les combinaisons ayant un coût supérieur à notre argent
        s = list(i for i in s if i[1] <= W)
        # Ressort la combinaison avec le bénéfice maximal
        if len(s) != 0:
            d = max(s, key=lambda x: x[2])
            if d[2] > maxy[2]:
                maxy = d
    end = time.time()
    timing = end - start
    print(j, timing)
    study_list.append([j, round(float(timing), 5), maxy[-1]])

df_study=pd.DataFrame(study_list, columns=["i", "timing", "profit"])

writer = pd.ExcelWriter('brute_force_2.xlsx', engine='xlsxwriter')
df_time = df_study["timing"]
df_profit = df_study["profit"]
df_time.to_excel(writer, sheet_name='time', index=False)
df_profit.to_excel(writer, sheet_name='profit', index=False)
writer.save()