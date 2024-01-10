import numpy as np
import matplotlib.pyplot as plt

group1 = np.zeros(4)
group2 = np.zeros(4)
group3 = np.zeros(4)

group1 = (1.60, 1.85, 1.75, 1.80)
group2 = (0.50, 0.70, 1.90, 1.75)
group3 = (1, 2, 3, 4)

plt.plot(group3, group1, label="Group 1", color="red")
plt.plot(group3, group2, label="Group 2", color="blue")
plt.ylabel("Height (m)")
plt.xlabel("Number")
plt.axis([0, 5, 0, 2])
plt.legend()
plt.show()