'''用python设计的第一个游戏'''

temp = input("不妨猜一下小甲鱼心里想的是哪个数字：")
guess = int(temp)

if(guess == 8):
    print("你是小甲鱼心里的蛔虫吗？")
else:
    if guess < 8:
        print("小啦~")
    else:
        print("大啦~")
print("游戏结束不玩了")

while 1 < 2:
    print("ilovefishc.com")

counts = 3;
while counts > 0:
    print("ilovefishc.com")
    counts = counts - 1


"""用python设计的第一个小游戏"""

counts = 3;

while counts > 0:
    temp = input("不妨猜一下小甲鱼心里想的是哪个数字：")
    guess = int(temp)

    if(guess == 8):
        print("你是小甲鱼心里的蛔虫吗？")
    else:
        if guess < 8:
            print("小啦~")
        else:
            print("大啦~")
    counts = counts - 1
print("游戏结束不玩了")

"""用python设计的第一个小游戏"""

counts = 3;

while counts > 0:
    temp = input("不妨猜一下小甲鱼心里想的是哪个数字：")
    guess = int(temp)

    if(guess == 8):
        print("你是小甲鱼心里的蛔虫吗？")
        break
    else:
        if guess < 8:
            print("小啦~")
        else:
            print("大啦~")
    counts = counts - 1
print("游戏结束不玩了")
