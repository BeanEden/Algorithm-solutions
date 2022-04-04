from functionsTest import creation_dossier_categorie, rows_list, value_cleaner, csv_read_threaded, threaded_clean_list, merge_sort, knapSackList
import time
import math

list_csv_threaded = csv_read_threaded("C:\opc finis\Projet 7\dataset2_Python+P7.csv")
start = time.time()
list_clean = threaded_clean_list(list_csv_threaded)
list_test = merge_sort(list_clean)
end = time.time()
timing = end-start
print(timing)
print(len(list_test))
n = len(list_test)

W = 500

start = time.time()
# result_minus = knapSackList(W, short_list, n)
result_minus = knapSackList(W, list_test, n)
print(result_minus)
end = time.time()
timing = end-start
print(timing)

fichier_csv = rows_list(W, list_test, n)
path = creation_dossier_categorie(fichier_csv)



