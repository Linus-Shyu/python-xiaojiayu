import random 
random.randint(1,10)

random.randint(100,10000)

"""用python开发的第一个小游戏"""

import random

counts = 3
answer = random.randint(1,10)

while counts > 0:
    temp = input("不妨猜猜小甲鱼心里想的是哪个数字：")
    guess = int(temp)

    if guess == answer:
        print("你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
        break
    else:
        if guess < answer:
            print("小啦～")
        else:
            print("大啦～")
        counts = counts - 1
print("游戏结束不玩了^_^")

x = random.getstate()
print(x)
random.randint()
random.randint()
random.randint()
random.randint()
random.randint()

random.setstate(x)
random.randint()
random.randint()
random.randint()
random.randint()
random.randint()