#这是什么玩意儿？
result_list = []

for i1 in range(2,4,2):
    for i2 in range(0,9,2):
        for i3 in range(0,9,2):
            for i4 in range(0,9,2):
                result = i1 * 1000 + i2 * 100 + i3 * 10 + i4
                result_list.append(result)
                print(result)

result_sum = sum(result_list)
print(result_sum)
print(len(result_list))