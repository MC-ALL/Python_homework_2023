import numpy as np
import math

x = np.linspace(-math.pi / 2, math.pi / 2, 100)
y = [math.sin(i) for i in x]

csv_date = np.vstack((x, y)).T
csv_date_nonT = np.vstack((x, y))

np.savetxt("data.csv", csv_date, delimiter=",")
np.savetxt("data_nonT.csv", csv_date_nonT, delimiter=",")

csv_date_in = np.loadtxt("data.csv", delimiter=",")
csv_date_nonT_in = np.loadtxt("data_nonT.csv", delimiter=",")

# print(csv_date_in)
# print(csv_date_nonT_in)

xin = csv_date_in[:, 0]
yin = csv_date_in[:, 1]
print(xin,yin)