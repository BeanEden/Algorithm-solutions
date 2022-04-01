import concurrent.futures

# Action-1 	20 	5%
# Action-2 	30 	10%
# Action-3 	50 	15%
# Action-4 	70 	20%
# Action-5 	60 	17%
# Action-6 	80 	25%
# Action-7 	22 	7%
# Action-8 	26 	11%
# Action-9 	48 	13%
# Action-10 	34 	27%
# Action-11 	42 	17%
# Action-12 	110 	 9%
# Action-13 	38 	23%
# Action-14 	14 	1%
# Action-15 	18 	3%
# Action-16 	08 	8%
# Action-17 	04 	12%
# Action-18  	10 	14%
# Action-19 	24  	21%
# Action-20 	114 	18%


d = {
    "Action-1": [20, 0.05],
    "Action-2": [30, 0.1],
    "Action-3": [50, 0.15],
    "Action-4": [70, 0.2],
    "Action-5": [60, 0.17],
    "Action-6": [80, 0.25],
    "Action-7": [22, 0.07],
    "Action-8": [26, 0.11],
    "Action-9": [48, 0.13],
    "Action-10": [34, 0.27],
    "Action-11": [42, 0.17],
    "Action-12": [110, 0.09],
    "Action-13": [38, 0.23],
    "Action-14": [14, 0.01],
    "Action-15": [18, 0.03],
    "Action-16": [8, 0.08],
    "Action-17": [4, 0.12],
    "Action-18": [10, 0.14],
    "Action-19": [24, 0.21],
    "Action-20": [114, 0.18]
}

for key, value in d.items():
    benefit = value[0]*value[1]
    value.append(float(benefit))
# print(d)

fullMoney = 500
for key, value in d.items():
    ratio = value[0]/fullMoney
    value.append(float(ratio))
# print(d)

for key, value in d.items():
    ratio_full = value[1]*value[3]
    value.append(float(ratio_full))
# print(d)





list_test = ["action1", "action2", "action3", "action4", "action5"]
# lets = choose_iter(list_test, 5)
#
# for i in lets:
#     print(i)

# length = 3
# listable = []
# for i in range(len(list_test)):
#         for next in choose_iter(list_test[i+1:len(list_test)], length-1):
#             print("next" + str(next) + str(length-1))
#             listable.append([list_test[i],] + next)
#             print("listable" +str(listable))



#
# def force_brute_optim(i_arg,listy,listi, W, maxy):
#     s = list(map(lambda x: (x, sum(map(lambda j: listy[j][0], x)), round(float(sum(map(lambda k: listy[k][1], x))), 2)),
#                  choose_iter(listi, i_arg)))
#     s = list(i for i in s if i[1] <= W)
#     if len(s) != 0:
#         d = max(s, key=lambda x: x[2])
#         if d[2] > maxy[2]:
#             maxy = d
#     return maxy
#
# # force_brute_optim(len(listy), listy, listi, 500)
# # print("maxy" + str(maxy))
# def global_funct(listy,listi, W):
#     maxy = ["", 0, 0]
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         a = list(executor.map(lambda x : force_brute_optim(x,listy,listi,W, maxy),range(1, 21)))
#     return maxy
#
# # amen = global_funct(listy,listi,W)
# # print(amen)
#
#
# def knapSack(W, wt, val,n):
#     if n == 0 or W == 0:
#         return 0
#     if (wt[n-1] > W):
#         return knapSack(W, wt, val, n-1)
#
#     else:
#         return max(
#             val[n-1] + knapSack(
#                 W-wt[n-1], wt, val, n-1),
#             knapSack(W, wt, val, n-1))


# a = knapSack(W, wt, val,len(val))
# print("a - " + str(a))



# listy=[2,3,5,8]
# print("listy -" +str(listy))
#
#
# listy_str=[]
# for i in listy:
#     listy_str.append(str(i))
#
# print("listy_str -" +str(listy_str))
#
# def multiply_5(i):
#     return i*5
#
# listy=list(map(lambda x:x*5,listy))
# print("listy -" +str(listy))