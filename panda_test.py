from functions import creation_dossier_category, merge_sort, print_result, knap_sack_list_name, csv_read_threaded, threaded_clean_list, rows_list
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display

fold = 1
W = 500

file = "C:\opc finis\Projet 7\dataset1_Python+P7.csv"

start_read_time = time.time()
list_csv_threaded = csv_read_threaded(file)
end_read = time.time()

start_clean_time = time.time()
list_clean = threaded_clean_list(list_csv_threaded)
end_clean = time.time()
list_clean = merge_sort(list_clean)
n = len(list_clean)

df_time = pd.DataFrame(data=None)
df_cumsum_time = pd.DataFrame(data=None)
df_profit = pd.DataFrame(data=None)

for i in range(10):
    table = rows_list(W, list_clean, n)
    df_interm = pd.DataFrame(table, columns=["i", "timing", "benefice", "nb_actions"])
    df_cumsum_time["cum_sum"+str(i)] = df_interm["timing"].cumsum()
    df_time["timing_run_"+str(i)] = df_interm["timing"]
    df_profit["profit_run_"+str(i)] = df_interm["benefice"]
    print(i)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('run_file_1.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df_time.to_excel(writer, sheet_name='time', index=False)
df_cumsum_time.to_excel(writer, sheet_name='tim_sum', index=False)
df_profit.to_excel(writer, sheet_name='profit', index=False)
# Close the Pandas Excel writer and output the Excel file.
writer.save()

# print(table)

# print(df)
# #
# # df = pd.DataFrame(
df_cumsum_time['average'] = df_cumsum_time.mean(numeric_only=True, axis=1)
lines = df_cumsum_time['average'].plot.line()
profit_line = df_profit.plot.line()
plt.show()