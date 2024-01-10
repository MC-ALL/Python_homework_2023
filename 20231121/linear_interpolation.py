#插值函数
def interpolation(x_y, t):
    x_t = int(t)
    y1 = x_y[x_t]
    y2 = x_y[x_t + 1]
    y_t = y1 + (t - x_t) * (y2 - y1) / 1
    return y_t

#查找打印函数
def print_find(x_y):
    while True:
        user_input = float(input("请输入要查找的数字（输入负数退出）："))
        if user_input >= 0:
            print(interpolation(x_y, user_input))
        else:
            print("退出程序")
            break

x_y = {0:4.4, 1:2.0, 2:11.0, 3:21.5, 4:7.5}

print_find(x_y)