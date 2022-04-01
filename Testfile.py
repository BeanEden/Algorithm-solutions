from functionsTest import knapSack_try, knapSackList, merge_sort, csv_read_threaded, csv_read, mergeSortList, glouton,knapSack, knapSackName, mergeSort, quickSort,quickSortHelper,partition, choose_iter, val_list
from panda import df_duplicate

df_reduced = df_duplicate.head(n=15)
# print(df_reduced)
data_dict = df_reduced.to_dict("index")
W = 500
# listy = {key : tuple(map(lambda v : (v["price"], v["benefit"]),value) for key, value in data_dict.items()}
# listy_test =tuple(map(lambda v : (v["price"], v["benefit"]),value) for value in data_dict.values())
# print(listy)

listy = {}
for key, value in data_dict.items():
    listy[key] = (value["price"], value["benefit"])
# print(listy)

listi = list(map(lambda x : x,data_dict))
wt = list(map(lambda x : x[1]["price"],data_dict.items()))
val = list(map(lambda x : x[1]["benefit"],data_dict.items()))
# n = len(val)
#
# result = knapSackName(W, wt, val, n,listi)
# print(result)


# merge_example = mergeSort(wt)
# print(merge_example)
#
# merge_dict = mergeSortDict(data_dict)
# print(merge_dict)
# result_name = knapSackName(W, wt, val, n, listi)
# print(result_name)
# print(val_list)

maxy = ["", 0, 0]

list_csv = csv_read("C:\opc finis\Projet 7\dataset1_Python+P7.csv")

list_csv_threaded = csv_read_threaded("C:\opc finis\Projet 7\dataset1_Python+P7.csv")
# print(list_csv_threaded)

list_test = merge_sort(list_csv_threaded)
n = 20
length = len(list_test)-n
short_list = list_test[length:]

name_list = list(map(lambda x : x[0], short_list))
wt_list = list(map(lambda x : x[1], short_list))
val_list = list(map(lambda x : x[-1], short_list))



result_try = knapSack_try(W, wt_list, val_list, n)
print(result_try)

result_list = knapSack(W, wt_list, val_list, n)
print(result_list)

# result_2 = knapSackList(W, short_list,n)
# print(result_2)
#
# test_glouton = glouton(short_list, 500)
#
# print(test_glouton)

# print_list = list(map(lambda x:print(x), short_list))
# merged_list = mergeSortList(list_csv)
# print(merged_list)
# for i in range(1, n+1):
#     s = list(map(lambda x: (x, sum(map(lambda j: listy[j][0], x)), round(float(sum(map(lambda k: listy[k][1], x))),2)), choose_iter(listi, i)))
#     s = list(i for i in s if i[1] <= W)
#     if len(s) != 0:
#         d = max(s, key=lambda x: x[2])
#         if d[2] > maxy[2]:
#             maxy = d
# print(maxy)