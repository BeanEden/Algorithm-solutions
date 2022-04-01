from functionsTest import knapSacktest, knapSackList_deux, knapSackList, merge_sort, csv_read_threaded, csv_read, mergeSortList, glouton,knapSack, knapSackName, mergeSort, quickSort,quickSortHelper,partition, choose_iter, val_list
import time
import math

list_csv_threaded = csv_read_threaded("C:\opc finis\Projet 7\dataset1_Python+P7.csv")

list_test = merge_sort(list_csv_threaded)
n = 20
length = len(list_test)-n
short_list = list_test[length:]
print(short_list)
W = 500

# test_glouton = glouton(short_list, W)
# print(test_glouton)

# result_2 = knapSackList(W, short_list,n)
# print(result_2)

actions = []
start = time.time()
result_minus = knapSackList(W, short_list, n)
print(result_minus)
end = time.time()
timing = end-start
print(timing)
print(timing/n)

n2 = 25
length2 = len(list_test)-n2
short_list2 = list_test[length2:]
start2 = time.time()
result_minus2 = knapSackList(W, short_list2, n2)
print(result_minus2)
end2 = time.time()
timing2 = end2-start2
print(timing2)
print(timing2/n2)

time_spent = timing2/timing
rapport = n2/n

print(time_spent, rapport)

ar = 5*math.log(5)
print(ar)