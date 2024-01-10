import numpy as np
import matplotlib.pyplot as plt


def check_error(x, y, a, b):
    error = 0
    for i in (x):
        i = int(i)
        error += (a * x[i] + b - y[i]) ** 2
    return error

def fit_compute(x, y):
    sum_x = sum_y = a = b = p = q = 0
    for i in x:
        sum_x += i
    for i in y:
        sum_y += i
    arg_x = sum_x / len(x)
    arg_y = sum_y / len(y)
    for i in range(len(x)):
        p += (x[i] - arg_x) * (y[i] - arg_y)
        q += (x[i] - arg_x) ** 2
    a = p / q
    b = arg_y - a * arg_x
    return a, b

def auto_find(x, y):
    error_record = a_record = b_record = 20
    for a in np.arange(0, 1.5, 0.001):
        for b in np.arange(-0.5, 0.5, 0.001):
            error = check_error(x, y, a, b)
            if error < error_record:
                error_record = error
                a_record = a
                b_record = b
    return a_record, b_record

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.5, 2.0, 1.0, 1.5, 7.5])

# while True:
#     a = float(input("输入a："))
#     b = float(input("输入b："))
#     error = check_error(x, y, a, b)
#     print("error:", error)

a_record, b_record = fit_compute(x, y)
error_record = check_error(x, y, a_record, b_record)
print("a:", a_record, " b:", b_record, " error:", error_record)

plt.scatter(x, y, label = "measure")
plt.plot(x, a_record * x + b_record, label = "fit")
plt.legend()
plt.show()

