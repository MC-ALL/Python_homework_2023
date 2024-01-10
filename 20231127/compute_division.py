N = 4

try:
    for i in range(N):
        while True:
            try:
                a = int(input("输入a: "))
                b = int(input("输入b: "))
                print("a / b = %f \n" % (a / b))
                break
            except ZeroDivisionError:
                print("除数不能为0")
            except ValueError:
                print("输入的不是整数")
except KeyboardInterrupt:
    print("用户强制中断")
