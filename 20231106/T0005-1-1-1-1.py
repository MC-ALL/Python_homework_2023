import numpy as np

t = np.linspace(0, 1, 1001)
y = 5 * t - 0.5 * 9.81 * t ** 2

init = y[0]
index = -1
max_index = 0

for i in y:
    index += 1
    if i > init:
        init = i
        max  = i
        max_index = index

print(max, max_index)


