import random

def check_illegal(guess, history, width):
    if (guess in history) or (guess < 1) or (guess > width):
        return True
    else:
        history.append(guess)
        return False

def game(width):
    
    print("初始化炸弹", end="\n\n")
    boom = random.randint(1, width)
    
    print("【游戏开始】 \n猜测从 1 到 %d 的数字" % width, end="\n\n")
    history = []
    count = 2
    
    while(True):
        
        print("【第 %d 回合】" % (count/2), end="\n\n")
        
        print("【你的回合】")   
        while(True):
            print("请输入猜测的数字：", end="")
            guess = int(input())
            if check_illegal(guess, history, width):
                print("无效的猜测，请重新输入")
                continue
            else:
                count += 1
                break            
        if guess == boom:
            print("恭喜你，你踩到了炸弹", end="\n\n")
            break
        else:
            print("你活了下来", end="\n\n")
            
                
        print("【电脑的回合】")
        while(True):
            guess = random.randint(1, width)
            if check_illegal(guess, history, width):
                continue
            else:
                count += 1
                break
        print("电脑猜测的数字是：%d" % guess)
        if guess == boom:
            print("电脑踩到了炸弹", end="\n\n")
            break
        else:
            print("电脑活了下来", end="\n\n")

    return count/2


if __name__ == "__main__":
    print("说明")
    print("游戏规则：")
    count = game(10)
    print("【游戏结束】")
    print("共进行了 %d 轮" % count, end="\n\n")
    pass