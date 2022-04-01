import csv
import concurrent.futures

def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)
    return alist

def mergeSortList(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        print(lefthalf[i][-1])
        print(righthalf[j][-1])
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][-1] <= righthalf[j][-1]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)
    return alist
# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)


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
        if left[0][2] < right[0][2]:
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


# def knapSacktest(W, liste, n, actions=[]):
#     if n == 0 or W == 0:
#         return 0,""
#     if (liste[n-1][1] > W):
#         return knapSackList(W, liste, n-1, actions)
#     else:
#         knapSack1 = knapSacktest(W - liste[n - 1][1], liste, n - 1, actions)[0]
#         print("valminusone - " + str(knapSack1))
#         knapSack2 = knapSacktest(W, liste, n - 1)[0]
#         print("valone - " + str(liste[n - 1][-1] + knapSack2))
#         if knapSack2 > liste[n-1][-1] + knapSack1 :
#             actions.append(liste[n-1][0])
#         return max(
#             liste[n-1][-1] + knapSackList(
#                 W-liste[n-1][1], liste, n-1),
#             knapSackList(W, liste, n-1)), actions

def knapSacktest(W, wt, val,ids,n):

    if n == 0 or W == 0:
        return 0,""
    if (wt[n-1] > W):
        return knapSack(W, wt, val,ids, n-1)

    else:
        knapsack1=knapSack(W-wt[n-1], wt, val,ids, n-1)
        knapsack2=knapSack(W, wt, val,ids, n-1)
        if  val[n-1]+knapsack1[0]>knapsack2[0]:
            return (val[n-1]+knapsack1[0],str(ids[n-1])+","+knapsack1[1])
        return knapsack2

# knapSack(W, wt, val,ids,len(val))


val_list = []
def knapSackName(W, wt, val,n, name_list):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSackName(W, wt, val, n-1,name_list)
    else:
        return max(
            val[n-1] + knapSackName(
                W-wt[n-1], wt, val, n-1, name_list),
            knapSackName(W, wt, val, n-1, name_list))

# def knapSackList(W, liste, n):
#     if n == 0 or W == 0:
#         return 0
#     if (liste[n-1][1] > W):
#         return knapSackList(W, liste, n-1)
#     else:
#         # print(liste[n-1][2])
#         return max(
#             liste[n-1][-1] + knapSackList(
#                 W-liste[n-1][1], liste, n-1),
#             knapSackList(W, liste, n-1))

def knapSackList(W, liste, n):
    if n == 0 or W == 0:
        return 0,""
    if (liste[n-1][1] > W):
        return knapSackList(W, liste, n-1)
    else:
        # print(liste[n-1][2])
        knapSack1 = knapSackList(W-liste[n-1][1], liste, n-1)
        knapSack2 = knapSackList(W, liste, n-1)
        if liste[n-1][-1] + knapSack1[0] > knapSack2[0]:
            return (liste[n-1][-1] + knapSack1[0], str(liste[n-1][0] + ", "+knapSack1[1]))
        return knapSack2


def knapSackList_deux(W, liste, n):
    if n == 0 or W == 0:
        return 0, ""
    if (liste[n-1][1] > W):
        return knapSackList_deux(W, liste, n-1)
    else:
        val_minus_one = knapSackList_deux(W - liste[n - 1][1], liste, n - 1)
        print("valminusone - " +str(val_minus_one))

        val_one = knapSackList_deux(W, liste, n - 1)
        print("valone - " +str(liste[n-1][-1] + val_one))

        if liste[n-1][-1] + val_minus_one[0] > val_one[0]:
            return liste[n-1][-1] + val_minus_one[0], val_minus_one[1] + "-" + liste[n-1][0]
        else:
            return val_one[0], val_one[1]


def knapSack_try(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] # Build table K[][] in bottom to up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if (i == 0 or w == 0):
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][int(w-wt[i-1])],
                K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W] # Driver code




def glouton(liste, taille_max):
    reponse = []
    total_benefit = 0
    prix = 0
    i = 0
    while i < len(liste) and prix <= taille_max:
        # nom, d, t = liste[i]
        p = liste[i][1]
        if prix + p <= taille_max:
            reponse.append(liste[i][0])
            prix += p
            total_benefit += liste[i][-1]
            i += 1
    return reponse, round(float(prix),2), total_benefit


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

# alist = [54,26,93,17,77,31,44,55,20]
# quickSort(alist)
# print(alist)

def choose_iter(elements, length):
    # print(elements)
    for i in range(len(elements)):
        if length == 1:
            yield [elements[i],]
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                # print(str(next) + str(length-1))
                yield [elements[i],] + next

def csv_read(file):
    list_csv = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        header = next(spamreader)
        for row in spamreader:
            benefit = [round(float((float(row[1])*float(row[2])/100)),2)]
            indice = row + benefit
            list_csv.append(indice)
    return list_csv

def csv_read_threaded(file):
    list_csv = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        header = next(spamreader)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # list_csv = list(executor.map(lambda x : [x[0], float(x[1]), float(x[2])] + [round(float((float(x[1]) * float(x[2]) / 100)), 2)], spamreader))
            list_csv = list(executor.map(lambda x: benefit_row_calculator(x), spamreader))
            # list_csv = list(executor.map(lambda x: [x[0], float(x[1]), float(x[2])], spamreader))
    return list_csv

def benefit_row_calculator(row):
    row_calculated = [row[0], float(row[1]), float(row[2])] + [round(float((float(row[1]) * float(row[2]) / 100)), 2)]
    return row_calculated