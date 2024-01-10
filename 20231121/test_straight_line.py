import random

def check(x, c):
    if x != c:
        f_x = 4 * x + 1
        f_c = 4 * c + 1
        print((f_x - f_c) / (x - c))

for i in range(100):
    x = random.randrange(1, 100)
    check(x, 2)
