from functions import complete_algorithm, creation_dossier_category, merge_sort, print_result, knap_sack_list_name, csv_read_threaded, threaded_clean_list, rows_list
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display

fold = 1
W = 500

file = "C:\opc finis\Projet 7\dataset1_Python+P7.csv"
list_csv_threaded = csv_read_threaded(file)
list_clean = threaded_clean_list(list_csv_threaded)
list_clean = merge_sort(list_clean)
n = len(list_clean)

study_list =[]
df_time = pd.DataFrame(data=None)
df_profit = pd.DataFrame(data=None)

for i in range(n):
    start_time = time.time()
    list_csv_threaded = csv_read_threaded(file)
    r = complete_algorithm(W, list_csv_threaded, start_time,i)
    study_list.append([r[1], r[0][1]])
    print(i)


df_study=pd.DataFrame(study_list, columns=["timing", "profit"])
writer = pd.ExcelWriter('study_file1_unsorted.xlsx', engine='xlsxwriter')
df_time = df_study["timing"]
df_profit = df_study["profit"]
df_time.to_excel(writer, sheet_name='time', index=False)
df_profit.to_excel(writer, sheet_name='profit', index=False)
writer.save()

