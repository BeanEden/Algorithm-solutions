from functions import complete_algorithm, csv_read_threaded
import time

W = 500
fold = 1
file = "C:\opc finis\Projet 7\data\dataset1_Python+P7.csv"

start_one = time.time()
list_csv_threaded = csv_read_threaded(file)
complete_algorithm(W, list_csv_threaded, start_one, fold)

print("")

file_two = "C:\opc finis\Projet 7\data\dataset2_Python+P7.csv"

start_two = time.time()
list_csv_threaded_two = csv_read_threaded(file_two)
complete_algorithm(W, list_csv_threaded_two, start_two, fold)

