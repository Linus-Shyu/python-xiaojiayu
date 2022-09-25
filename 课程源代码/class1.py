"""用python设计的第一个游戏"""

temp = input("不妨猜猜小甲鱼心里想的是那个数字")
guess = int(temp)

if(guess == 8):
    print("你是小甲鱼心里的蛔虫吗")
else:
    print("哼，猜对了也没有奖励！")

print("游戏结束不玩儿了。")