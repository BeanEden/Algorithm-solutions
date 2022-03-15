import concurrent.futures

def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield [elements[i], ]
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield [elements[i], ] + next

string_ = "Action-1:20:1;Action-2:30:3;Action-3:50:7,5;Action-4:70:14;Action-5:60:10,2;Action-6:80:20;Action-7:22:1,54;Action-8:26:2,86;Action-9:48:6,24;Action-10:34:9,18;Action-11:42:7,14;Action-12:110:9,9;Action-13:38:8,74;Action-14:14:0,14;Action-15:18:0,54;Action-16:8:0,64;Action-17:4:0,48;Action-18:10:1,4;Action-19:24:5,04;Action-20:114:20,52"

with concurrent.futures.ThreadPoolExecutor() as executor:
    listi = list(executor.map(lambda x: x.split(":")[0], string_.split(";")))

with concurrent.futures.ThreadPoolExecutor() as executor:
    listy = {i.split(":")[0]: tuple(executor.map(lambda x: round(float(x), 2), i.split(":")[1:])) for i in string_.replace(",", ".").split(";")}


with concurrent.futures.ThreadPoolExecutor() as executor:
    wt = list(executor.map(lambda x: listy[x][0], listi))


with concurrent.futures.ThreadPoolExecutor() as executor:
    val = list(executor.map(lambda x: listy[x][1], listi))


W = 500

# def agglomerat(listy_arg, listi_arg):
#     maxy = ["", 0, 0]
#     length = len(listy)+1
#     for i in range(1, length):
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             s = list(executor.map(lambda x: (x, sum(map(lambda i: listy_arg[i][0], x)), sum(map(lambda i: listy_arg[i][1], x))),
#                          choose_iter(listi_arg, i)))
#         s = list(i for i in s if i[1] <= W)
#         if len(s) != 0:
#             d = max(s, key=lambda x: x[2])
#             if d[2] > maxy[2]:
#                 maxy = d
#     return maxy


# def agglomerat(listy_arg, listi_arg, maxy_arg):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         for i in range(1, 21):
#             s = list(executor.map(lambda x: (x, sum(executor.map(lambda i: listy_arg[i][0], x)), sum(executor.map(lambda i: listy_arg[i][1], x))), choose_iter(listi_arg, i)))
#             s = list(i for i in s if i[1] <= W)
#             if len(s) != 0:
#                 d = max(s, key=lambda x: x[2])
#                 if d[2] > maxy_arg[2]:
#                     maxy_arg = d
#     return maxy_arg

# def general_agglo(listy_arg, listi_arg):
#     maxy = ["", 0, 0]
#     length = len(listy)+1
#     a = agglomerat(listy_arg, listi_arg, maxy)
#     return a

# max = general_agglo(listy,listi)
# maxy = ["", 0, 0]
# # print(maxy)
# for i in range(1, 21):
#     s = list(map(lambda x: (x, sum(map(lambda y: listy[y][0], x)), sum(map(lambda j: listy[j][1], x))), choose_iter(listi, i)))
#     s = list(i for i in s if i[1] <= W)
#     if len(s) != 0:
#         d = max(s, key=lambda x: x[2])
#         if d[2] > maxy[2]:
#             maxy = d

def functionDone(listy, listi):
    maxy = ["", 0, 0]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        list_ = list(executor.map(lambda x: agglomerat(listy, listi, maxy, x), range(1,21)))
    return list_

def agglomerat(listy_arg, listi_arg, maxy_arg, i):
    with concurrent.futures.ThreadPoolExecutor() as executor:
            s = list(executor.map(lambda x: (x, sum(executor.map(lambda i: listy_arg[i][0], maxy_arg)), sum(executor.map(lambda i: listy_arg[i][1], x))), choose_iter(listi_arg, i)))
            s = list(i for i in s if i[1] <= W)
            if len(s) != 0:
                d = max(s, key=lambda x: x[2])
                if d[2] > maxy_arg[2]:
                    maxy_arg = d
    return maxy_arg

maxy = ["", 0, 0]
range_ = range(1,21)
range_list = [1]*(+=1)
print(range_list)
# list_ = list(executor.map(lambda x: agglomerat(listy, listi, maxy, x), range(1, 21)))
# a = functionDone(listy, listi)

# print(list_)
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     list(executor.map(lambda i: agglomerat(listy, listi, maxy, i)) for i in range(1, 21))
#
# for i in range(1, 21):
#     agglomerat(listy, listi, maxy, i)


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     tables = list(executor.map(lambda x: creation_un_livre(x), liste_url))


def knapSack(W, wt, val,n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))

a = knapSack(W, wt, val,len(val))
print("a - " + str(a))