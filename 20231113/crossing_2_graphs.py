import numpy as np

def compare(x, ecase):
    result = abs(x ** 2 - x)
    if result < ecase:
        return x
    else:
        return None

n = 400
ecase = 0.01
x = np.linspace(-4, 4,n)
result = []

for i in x:
    x0 = compare(i, ecase)
    if x0 is not None:
        print(i)
        result.append(x0)

print(result)