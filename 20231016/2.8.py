import random

group = []

for i in (1, 2, 3, 4):
    while True:
        r = random.randint(0, 10)
        if r not in group:
            group.append(r)
            break

print(group)