import timeit
import numpy as np

def add(a, b):
    return a + b

def mul(a, b):  
    return a * b

x =  np.zeros(10000)
y =  np.zeros(10000)

t = timeit.Timer("for i in range(len(x)): x[i] = mul(i, i + 1)", "from __main__ import mul, x")
x = t.timeit(10000)
print('Time, function call: {:g} seconds. '.format(x))

t = timeit.Timer("for i in range(len(y)): y[i] = add(i, i + 1)", "from __main__ import add, y")
y = t.timeit(10000)
print('Time, function call: {:g} seconds. '.format(y))
