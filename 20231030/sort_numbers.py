import random


def bobblesort(list):
    l = len(list)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

list = []

for i in range(6):
    list.append(random.randint(1, 10))

print(list)
bobblesort(list)
print(list)