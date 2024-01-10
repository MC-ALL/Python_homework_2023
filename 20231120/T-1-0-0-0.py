import random

#全局变量
point_list = []

def gen_number():
    number = random.randint(1, 9)
    return number

def check_answer(user_input, num1, num2):
    if user_input == num1 * num2:
        print("正确")
        #输出分数
        point_list.append(1)
    else:
        print("错误")
        #输出分数
        point_list.append(0)

#计数循环
i = 0
while i < 5:
    #生成数字
    num1 = gen_number()
    num2 = gen_number()
    #捕获输入
    try:
        user_input = int(input("输入 %d X %d 的答案：" % (num1, num2)))
        #检查输入
        check_answer(user_input, num1, num2)
        i += 1
    except:
        print("输入错误")
        user_input = 0
    
#打印结果
print(point_list)