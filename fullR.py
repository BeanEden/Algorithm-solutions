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


d2 = dict(sorted(d.items(), key=lambda x: x[-1]))

for key, value in d2.items():
    print(value)