import pandas as pd

file = "C:\opc finis\Projet 7\dataset1_Python+P7.csv"
a = pd.read_csv(file, index_col=0, low_memory=False)



print(a)