import random

N = int(input())
M = 0
number_list = []

for i in range(N):
    x = random.randint(1, 6)
    print(x)
    number_list.append(x)

for i in number_list:
    if i == 6:
        M += 1

print(M)
print(M / N)