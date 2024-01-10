import math

def polyarea(x, y):
    sum_1 = x[-1] * y[0]
    sum_2 = y[-1] * x[0]
    
    for i in range(len(x) -1):
        sum_1 += x[i] * y[i + 1]

    for i in range(len(y) -1):
        sum_2 += y[i] * x[i + 1]

    return 0.5 * abs(sum_1 - sum_2)

if __name__ == "__main__":

    # 三角形
    x = [0, 0, 1]
    y = [0, 1, 1]
    print(polyarea(x, y))

    # 正方形
    x = [0, 0, 1, 1]
    y = [0, 1, 1, 0]
    print(polyarea(x, y))

    # 五边形
    x = [0, 1, 1, 0.5, 0]
    y = [0, 0, 1, 2, 1]
    print(polyarea(x, y))