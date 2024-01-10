#import numpy as np
#import matplotlib.pyplot as plt

#v0 = 5
#g = 9.81
#t = np.linspace(0, 1, 1000)
#y = v0 * t - 0.5 * g * t ** 2
y = [1, 23, 123, 34]
largest_height = y[0]

for i in range(1, len(y), 1):
    print(i, largest_height)
    if y[i] > largest_height:
        largest_height = y[i]
        

print(largest_height)

#print("The largest height achieved was {:g} m".format(largest_height))

#plt.plot(t, y)
#plt.xlabel("Time (s)")
#plt.ylabel("Height (m)")
#plt.show()