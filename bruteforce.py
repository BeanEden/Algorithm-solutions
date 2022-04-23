import time


# Liste des actions
list_ = "Action-1:20:1;Action-2:30:3;Action-3:50:7,5;Action-4:70:14;Action-5:60:10,2;" \
        "Action-6:80:20;Action-7:22:1,54;Action-8:26:2,86;Action-9:48:6,24;Action-10:34:9,18;" \
        "Action-11:42:7,14;Action-12:110:9,9;Action-13:38:8,74;Action-14:14:0,14;Action-15:18:0,54;" \
        "Action-16:8:0,64;Action-17:4:0,48;Action-18:10:1,4;Action-19:24:5,04;Action-20:114:20,52"


# Créé un tuple (prix de l'action, bénéfice(valeur))
listy = {i.split(":")[0]: tuple(map(lambda x: round(float(x), 2), i.split(":")[1:]))
         for i in list_.replace(",", ".").split(";")}


# Liste des noms des actions
listi = list(map(lambda x: x.split(":")[0], list_.split(";")))


# Liste au format de la réponse finale ["Actions", coût total, bénéfice]
maxy = ["", 0, 0]
W = 500
n = len(listy)


def choose_iter(elements, length):
    """Fonction génératrice des itérateurs correspondants aux combinaisons possibles"""
    for i in range(len(elements)):
        if length == 1:
            yield [elements[i], ]
        else:
            for next_element in choose_iter(elements[i+1:len(elements)], length-1):
                yield [elements[i], ] + next_element


# Algorithme de force brute
start = time.time()

for i in range(1, n+1):
    # Pour chaque combinaison, calcule le coût total et bénéfice
    s = list(map(lambda x: (x,
                            sum(map(lambda j: listy[j][0], x)),
                            round(float(sum(map(lambda k: listy[k][1], x))), 2)),
                 choose_iter(listi, i)))
    # Retire les combinaisons ayant un coût supérieur à notre argent
    s = list(i for i in s if i[1] <= W)
    # Ressort la combinaison avec le bénéfice maximal
    if len(s) != 0:
        d = max(s, key=lambda x: x[2])
        if d[2] > maxy[2]:
            maxy = d

end = time.time()
timing = round(float(end-start), 2)

print(f"""Actions sélectionnées : {maxy[0]}
        Coût total : {maxy[1]}
        Bénéfice : {maxy[2]}
        Temps écoulé : {timing} secondes ({timing/n} s/n)""")

