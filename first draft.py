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
print(d)

fullMoney = 500
for key, value in d.items():
    ratio = value[0]/fullMoney
    value.append(float(ratio))
print(d)

for key, value in d.items():
    ratio_full = value[1]*value[3]
    value.append(float(ratio_full))
print(d)

def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield [elements[i],]
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield [elements[i],] + next

list_ = "Action-1:20:1;Action-2:30:3;Action-3:50:7,5;Action-4:70:14;Action-5:60:10,2;Action-6:80:20;Action-7:22:1,54;Action-8:26:2,86;Action-9:48:6,24;Action-10:34:9,18;Action-11:42:7,14;Action-12:110:9,9;Action-13:38:8,74;Action-14:14:0,14;Action-15:18:0,54;Action-16:8:0,64;Action-17:4:0,48;Action-18:10:1,4;Action-19:24:5,04;Action-20:114:20,52"
listi = list(map(lambda x: x.split(":")[0], list_.split(";")))
print(listi)

listy = {i.split(":")[0]: tuple(map(lambda x: round(float(x), 2), i.split(":")[1:])) for i in list_.replace(",", ".").split(";")}
print(listy)

wt = list(map(lambda x: listy[x][0], listi))
print("wt - " + str(wt))

val = list(map(lambda x: listy[x][1], listi))
print("val - " + str(val))
print(listy)

maxy = ["", 0, 0]
W = 500

for i in range(1, 21):
    s = list(map(lambda x: (x, sum(map(lambda i: listy[i][0], x)), sum(map(lambda i: listy[i][1], x))), choose_iter(listi, i)))
    s = list(i for i in s if i[1] <= W)
    if len(s) != 0:
        d = max(s, key=lambda x: x[2])
        if d[2] > maxy[2]:
            maxy = d

print("maxy" + str(maxy))

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

a = knapSack(W, wt, val,len(val))
print("a - " + str(a))

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