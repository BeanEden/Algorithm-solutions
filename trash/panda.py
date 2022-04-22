import pandas as pd
from functions import glouton,knapSack,mergeSort

file = "C:\opc finis\Projet 7\dataset1_Python+P7.csv"
# file = "C:\opc finis\Projet 7\dataset2_Python+P7.csv"

df = pd.read_csv(file, low_memory=False)
total_money = 500
df = df[df["price"] > 0]
df = df[df["profit"] > 0]
df = df.dropna(how="any")
average = df["profit"].mean()
df = df[df["profit"] > average]
# df["name"] = df.index()
# test = df.sort_index()
df["benefit"] = (df["price"]*df["profit"]/100).round(2)
df["ratio"] = (df["price"]/total_money/df["benefit"]/df["price"]*10000).round(2)
df_sorted = df.sort_values(by=["profit"], ascending=False)

# print(average)
#
# print(df_sorted)
df_sorted2 = df.sort_values(by=["ratio"], ascending=False)
# print(df_sorted2)
df_duplicate = df_sorted.drop_duplicates(subset='name', keep="first")
df_duplicate = df_duplicate.set_index("name")
df_duplicate = df_duplicate.sort_values(by=["benefit"], ascending=False)
# print(df_duplicate)
df_duplicate.to_csv("C:\opc finis\Projet 7\dataset1.csv")
# data_dict = df_duplicate.to_dict("index")
# print(data_dict)


