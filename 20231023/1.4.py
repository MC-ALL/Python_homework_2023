import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 3000)
print(x)

v = x**3
print(v)

plt.plot(x, v)
plt.show()