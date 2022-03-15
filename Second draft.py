list = []

def test_iterable(value):
    for i in range(0,value):
        yield i-1


def test_iterable_list(value):
    list=[]
    for i in range(0,value):
        list.append(i-1)

    return list

value_ = 10
test = test_iterable(value_)
test_list = test_iterable_list(value_)

for i in test:
    print(i)
print("================================")
for i in test_list :
    print(i)

sum_ = sum(test)
sum_2 = sum(test_list)
print("sum_ : " + str(sum_))
print("sum_2 : " + str(sum_2))