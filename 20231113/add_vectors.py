import numpy as np


def add_vectors(a, b):
    if np.linalg.norm(a) == np.linalg.norm(b):
        c = a + b
        return c
    else:
        return None
    
a = np.array([1, 2])
b = np.array([2, 1])
print(add_vectors(a, b))