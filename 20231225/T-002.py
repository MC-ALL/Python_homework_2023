import math
import numpy as np

def v(t):
    return 3 * t ** 2 * math.exp(t ** 3)

def V(t):
    return math.exp(t ** 3) - 1

def trap(y1, y2, dx):
    return (y1 + y2) * dx / 2

def sumInt(x):
    sum = 0
    for i in range(len(x) - 1):
        sum += trap(v(x[i]), v(x[i+1]), x[i+1] - x[i])
    return sum

x = np.linspace(0, 1, 10001)
print('sumInt is: {}'.format(sumInt(x)))
print('V is: {}'.format(V(1) - V(0)))
print('Error is: {}'.format(abs(sumInt(x) - (V(1) - V(0))))) 